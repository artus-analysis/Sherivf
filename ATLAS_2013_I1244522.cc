// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/PromptFinalState.hh"
#include "Rivet/Projections/LeadingParticlesFinalState.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/Projections/FastJets.hh"

namespace Rivet {


  /// @brief Measurement of isolated gamma + jet + X differential cross-sections
  class ATLAS_2013_I1244522 : public Analysis {
  public:

    // Constructor
    ATLAS_2013_I1244522()
      : Analysis("ATLAS_2013_I1244522")
    {  
      _eta_bins_areaoffset.push_back(0.0);
      _eta_bins_areaoffset.push_back(1.5);
      _eta_bins_areaoffset.push_back(3.0);
    }

  public:

    // Book histograms and initialise projections before the run
    void init() {
      FinalState fs;

      // Voronoi eta-phi tassellation with KT jets, for ambient energy density calculation
      FastJets fj(fs, FastJets::KT, 0.5);
      _area_def = new fastjet::AreaDefinition(fastjet::VoronoiAreaSpec());
      fj.useJetArea(_area_def);
      addProjection(fj, "KtJetsD05");

      // Leading photon
      LeadingParticlesFinalState photonfs(PromptFinalState(FinalState(-2.37, 2.37, 45.0*GeV)));
      photonfs.addParticleId(PID::PHOTON);
      addProjection(photonfs, "LeadingPhoton");

      // FS excluding the leading photon
      VetoedFinalState vfs(fs);
      vfs.addVetoOnThisFinalState(photonfs);
      addProjection(vfs, "JetFS");

      // Jets
      FastJets jetpro(vfs, FastJets::ANTIKT, 0.6);
      jetpro.useInvisibles();
      addProjection(jetpro, "Jets");

      _h_ph_pt      = bookHisto1D(1, 1, 1);
      _h_jet_pt     = bookHisto1D(2, 1, 1);
      _h_jet_rap    = bookHisto1D(3, 1, 1);
      _h_dphi_phjet = bookHisto1D(4, 1, 1);

      _h_costheta_biased_phjet = bookHisto1D(5, 1, 1);
      _h_mass_phjet            = bookHisto1D(6, 1, 1);
      _h_costheta_phjet        = bookHisto1D(7, 1, 1);

    }//init

    size_t getEtaBin(double eta_w) const {
      const double eta = fabs(eta_w);
      return binIndex(eta, _eta_bins_areaoffset);
    }

    // Perform the per-event analysis
    void analyze(const Event& event) {
      const double weight = event.weight();

      // Get the photon
      Particles photons = applyProjection<LeadingParticlesFinalState>(event, "LeadingPhoton").particles();
      if (photons.size() != 1 )  vetoEvent;
      const Particle& photon = photons[0];

      if (inRange(photon.abseta(), 1.37, 1.52))  vetoEvent;

      //Compute isolation energy in cone of radius .4 around photon (all particles)
      FourMomentum mom_in_EtCone;
      const Particles& fs = applyProjection<VetoedFinalState>(event, "JetFS").particles();
      foreach (const Particle& p, fs) {
        // Check if it's outside the cone of 0.4
        if (deltaR(photon, p) >= 0.4) continue;
        // Increment isolation energy
        mom_in_EtCone += p.momentum();
      }

      // Get the jet
      Jets jets, alljets = applyProjection<FastJets>(event, "Jets").jetsByPt(40.0*GeV);

      foreach (Jet jet, alljets)
        if (deltaR(photon, jet) > 1.0)  jets += jet;

      if (jets.empty())  vetoEvent;
      Jet leadingJet = jets[0];
      if (leadingJet.absrap() > 2.37)  vetoEvent;

      // Get the area-filtered jet inputs for computing median energy density, etc.
      vector<double> ptDensity, sigma, Njets;
      vector< vector<double> > ptDensities(_eta_bins_areaoffset.size()-1);
      FastJets fast_jets = applyProjection<FastJets>(event, "KtJetsD05");
      const fastjet::ClusterSequenceArea* clust_seq_area = fast_jets.clusterSeqArea();
      foreach (const Jet& jet, fast_jets.jets()) {
        const double area = clust_seq_area->area(jet);
        if (area > 10e-4 && jet.abseta() < _eta_bins_areaoffset.back())
          ptDensities.at( getEtaBin(jet.abseta()) ).push_back(jet.pT()/area);
      }

      // Compute the median energy density, etc.
      for (size_t b = 0; b < _eta_bins_areaoffset.size() - 1; ++b) {
        const int njets = ptDensities[b].size();
        const double ptmedian = (njets > 0) ? median(ptDensities[b]) : 0;
        const double ptsigma = (njets > 0) ? ptDensities[b][(size_t)(0.15865*njets)] : 0;
        ptDensity.push_back(ptmedian);
        sigma.push_back(ptsigma);
        Njets.push_back(njets);
      }

      // Compute the isolation energy correction (cone area*energy density)
      const double etCone_area = PI*sqr(0.4) - (5.0*.025)*(7.0*PI/128.);
      const double correction = ptDensity[getEtaBin(photon.abseta())] * etCone_area;

      // Apply isolation cut on area-corrected value
      if (mom_in_EtCone.Et() - correction >= 4*GeV)  vetoEvent;

      // Fill histos
      float photon_pt = photon.pT() * GeV;
      float jet_pt = leadingJet.pT() * GeV;
      float jet_y = leadingJet.absrap();
      float dphi_phj = deltaPhi(photon, leadingJet);
      float dy = deltaRap(photon, leadingJet);
      float mass_phj = (photon.momentum() + leadingJet.momentum()).mass() * GeV;
      float costheta_phj = tanh(dy/2);
      
	    _h_ph_pt->fill(photon_pt, weight); 
      _h_jet_pt->fill(jet_pt,   weight);
      _h_jet_rap->fill(jet_y,   weight);

      _h_dphi_phjet->fill(dphi_phj, weight);
      _h_costheta_biased_phjet->fill(costheta_phj, weight);

      if (mass_phj > 160.939) {
        if (fabs(photon.eta() + leadingJet.rap()) < 2.37) {
          if (costheta_phj < 0.829022) {
            _h_mass_phjet->fill(mass_phj,         weight);
            _h_costheta_phjet->fill(costheta_phj, weight);
          }
        }
      }
    }

    /// Normalise histograms etc., after the run
    void finalize() {
      const double sf( crossSection() / sumOfWeights() );
      scale(_h_ph_pt,                 sf);
      scale(_h_jet_pt,                sf);
      scale(_h_jet_rap,               sf);
      scale(_h_dphi_phjet,            sf);
      scale(_h_costheta_biased_phjet, sf);
      scale(_h_mass_phjet,            sf);
      scale(_h_costheta_phjet,        sf);
    }


  private:

    Histo1DPtr _h_ph_pt;
    Histo1DPtr _h_jet_pt;
    Histo1DPtr _h_jet_rap;
    Histo1DPtr _h_dphi_phjet;
    Histo1DPtr _h_costheta_biased_phjet;
    Histo1DPtr _h_mass_phjet;
    Histo1DPtr _h_costheta_phjet;

    fastjet::AreaDefinition* _area_def;

    std::vector<float> _eta_bins_areaoffset;

  };

  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(ATLAS_2013_I1244522);

}
