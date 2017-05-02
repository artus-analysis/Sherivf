// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Cuts.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/ZFinder.hh"
#include "Rivet/ProjectionApplier.hh"

#include "Rivet/Projections/IdentifiedFinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/JetAlg.hh"
#include "Rivet/Projections/VetoedFinalState.hh"

#include "Rivet/Math/Constants.hh"

#include "mcgrid/mcgrid.hh"

namespace Rivet {

/// @brief CMS Z boson rapidity measurement
/// modified to generate fastNLO files
class MCgrid_CMS_2015_Zee : public Analysis {
public:

	/// Constructor
	MCgrid_CMS_2015_Zee(): Analysis("MCgrid_CMS_2015_Zee"){}

public:
	/// Book histograms and initialise projections before the run
	void init() {


		const FinalState fs;




		// muon cuts
		Cut cut = (
			(Cuts::pT >= 27.*GeV)
			& (Cuts::etaIn(-2.3, 2.3))
		);
		// Z boson reconstruction
		ZFinder zfinder(FinalState(), cut, PID::MUON, 81.1876*GeV, 101.1876*GeV, 0.01, ZFinder::NOCLUSTER, ZFinder::NOTRACK);
		// register projections here
		addProjection(zfinder, "ZFinder");
		IdentifiedFinalState muons;
		muons.acceptId(PID::MUON);
		addProjection(muons, "Muons");
		
		//jet reconstruction without Z muon
		VetoedFinalState had_fs;
		had_fs.addVetoOnThisFinalState(getProjection<ZFinder>("ZFinder"));

		//projector (Initialisierung)
		addProjection(FastJets(had_fs, FastJets::ANTIKT, 0.4), "Jets");




		/// Book RIVET histograms
		std::vector<double> bin_edges = {40, 45, 50, 55, 60, 70, 75, 80, 90, 110, 130, 150, 170, 200, 250, 400}; 
		
		std::vector<double> bin_edges2; //For Correlation Plots
		std::vector<double> bin_edges_phistar2;
		bin_edges2.reserve(1000);
		bin_edges_phistar2.reserve(1000);
		for (int i=0; i<1000; i++){
			bin_edges2.push_back(i*10);
			bin_edges_phistar2.push_back(i*0.1);
		}
///		///Bins fuer phistar
		std::vector<double> bin_edges_phistar = {0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.115, 0.130, 0.145, 0.165, 0.190, 0.220, 0.26, 0.310, 0.350, 0.40, 0.45, 0.500, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0, 1.25, 1.5, 2, 3, 4, 6, 12, 25};

		/// bins for deltaphi
		std::vector<double> bin_edges_deltaphi;
		bin_edges_deltaphi.reserve(51);
		for (int i=0; i<=25; i++)
			bin_edges_deltaphi.push_back(i*((2*pi)/25.));


		m_ybins = {0.4, 0.8, 1.2, 1.6, 2.0, 2.4};


		

		_h_pTZ = bookHisto1D("zpt", bin_edges);     //alternative: bin_edges2
//		_h_yZ = bookHisto1D("zy", 46, -2.3, 2.3);
		_h_absyZ = bookHisto1D("abszy", 23, 0, 2.3);
//		_h_mZ = bookHisto1D("zmass", 20, 81, 101);
//		_h_phiZ = bookHisto1D("zphi", 32, -3.2, 3.2);

//		_h_pTmu = bookHisto1D("muminuspt", 20, 20, 120);
//		_h_etamu = bookHisto1D("muminuseta", 46, -2.3, 2.3);
//		_h_phimu = bookHisto1D("muminusphi", 32, -3.2, 3.2);

		_h_pTZ_0 = bookHisto1D("y0_zpt", bin_edges);
		_h_pTZ_1 = bookHisto1D("y1_zpt", bin_edges);
		_h_pTZ_2 = bookHisto1D("y2_zpt", bin_edges);
		_h_pTZ_3 = bookHisto1D("y3_zpt", bin_edges);
		_h_pTZ_4 = bookHisto1D("y4_zpt", bin_edges);
		_h_pTZ_5 = bookHisto1D("y5_zpt", bin_edges);
	
		_h_phistar_0 = bookHisto1D("y0_phistar", bin_edges_phistar);
                _h_phistar_1 = bookHisto1D("y1_phistar", bin_edges_phistar);
                _h_phistar_2 = bookHisto1D("y2_phistar", bin_edges_phistar);
                _h_phistar_3 = bookHisto1D("y3_phistar", bin_edges_phistar);
                _h_phistar_4 = bookHisto1D("y4_phistar", bin_edges_phistar);
                _h_phistar_5 = bookHisto1D("y5_phistar", bin_edges_phistar);

		/// book jet delta-phi histogram
//		_h_deltaphi = bookHisto1D("deltaphi", bin_edges_deltaphi);

		/// jet histogram (number of jets)
//		_h_njets = bookHisto1D("njets", 10, -0.5, 9.5);

///		/// Histogramm fuer phi_star buchen
		_h_phistar = bookHisto1D("phistar", bin_edges_phistar);


		/// Book fastNLO histograms/tables
		const string steeringFileName = "MCgrid_CMS_2015_Zee.str";

		MCgrid::subprocessConfig subproc(steeringFileName, MCgrid::BEAM_PROTON, MCgrid::BEAM_PROTON);

		MSG_INFO("Creating fastnloGridArch and fastnloConfig");
		MCgrid::fastnloGridArch arch_fnlo(20, 6, "Lagrange", "Lagrange", "sqrtlog10", "loglog025");

		const float center_of_mass_energy = 13000.;

		MCgrid::fastnloConfig config_fnlo(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_1(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_2(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_3(1, subproc, arch_fnlo, center_of_mass_energy);
///		
		MCgrid::fastnloConfig config_fnlo_phi(1, subproc, arch_fnlo, center_of_mass_energy);
		// in bins
		MCgrid::fastnloConfig config_fnlo_4(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_5(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_6(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_7(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_8(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_9(1, subproc, arch_fnlo, center_of_mass_energy);

		MCgrid::fastnloConfig config_fnlo_10(1, subproc, arch_fnlo, center_of_mass_energy);
                MCgrid::fastnloConfig config_fnlo_11(1, subproc, arch_fnlo, center_of_mass_energy);
                MCgrid::fastnloConfig config_fnlo_12(1, subproc, arch_fnlo, center_of_mass_energy);
                MCgrid::fastnloConfig config_fnlo_13(1, subproc, arch_fnlo, center_of_mass_energy);
                MCgrid::fastnloConfig config_fnlo_14(1, subproc, arch_fnlo, center_of_mass_energy);
                MCgrid::fastnloConfig config_fnlo_15(1, subproc, arch_fnlo, center_of_mass_energy);

		MSG_INFO("bookGrid. histoDir: " << histoDir());
		_fnlo_pTZ = MCgrid::bookGrid(_h_pTZ, histoDir(), config_fnlo);
		_fnlo_absyZ = MCgrid::bookGrid(_h_absyZ, histoDir(), config_fnlo_1);
//		_fnlo_yZ = MCgrid::bookGrid(_h_yZ, histoDir(), config_fnlo_2);
//		_fnlo_mZ = MCgrid::bookGrid(_h_mZ, histoDir(), config_fnlo_3);
///
		_fnlo_phistar = MCgrid::bookGrid(_h_phistar, histoDir(), config_fnlo_phi);

		_fnlo_pTZ_0 = MCgrid::bookGrid(_h_pTZ_0, histoDir(), config_fnlo_4);
		_fnlo_pTZ_1 = MCgrid::bookGrid(_h_pTZ_1, histoDir(), config_fnlo_5);
		_fnlo_pTZ_2 = MCgrid::bookGrid(_h_pTZ_2, histoDir(), config_fnlo_6);
		_fnlo_pTZ_3 = MCgrid::bookGrid(_h_pTZ_3, histoDir(), config_fnlo_7);
		_fnlo_pTZ_4 = MCgrid::bookGrid(_h_pTZ_4, histoDir(), config_fnlo_8);
	        _fnlo_pTZ_5 = MCgrid::bookGrid(_h_pTZ_5, histoDir(), config_fnlo_9);
        	
		_fnlo_phistar_0 = MCgrid::bookGrid(_h_phistar_0, histoDir(), config_fnlo_10);
                _fnlo_phistar_1 = MCgrid::bookGrid(_h_phistar_1, histoDir(), config_fnlo_11);
                _fnlo_phistar_2 = MCgrid::bookGrid(_h_phistar_2, histoDir(), config_fnlo_12);
                _fnlo_phistar_3 = MCgrid::bookGrid(_h_phistar_3, histoDir(), config_fnlo_13);
                _fnlo_phistar_4 = MCgrid::bookGrid(_h_phistar_4, histoDir(), config_fnlo_14);
                _fnlo_phistar_5 = MCgrid::bookGrid(_h_phistar_5, histoDir(), config_fnlo_15);
		MSG_INFO("fastnlo init done");
	}


	/// Perform the per-event analysis
	void analyze(const Event& event) {
		const ZFinder& zfinder = applyProjection<ZFinder>(event, "ZFinder");
		// Handle event
		MCgrid::PDFHandler::HandleEvent(event, histoDir());
		const double weight = event.weight();
		//const Particles particles = applyProjection<FinalState>(event, "Muons").particlesByPt(Cuts::pT>=0.5*GeV);		
		if (zfinder.bosons().size() == 1) {

			double yZ = zfinder.bosons()[0].momentum().rapidity();
			double pTZ = zfinder.bosons()[0].momentum().pT();
//			double mZ = zfinder.bosons()[0].momentum().mass();
//			double phiZ = zfinder.bosons()[0].momentum().phi()-pi;

		// find jets
		const FastJets& fj = applyProjection<FastJets>(event, "Jets");
		const Jets& jets = fj.jetsByPt(Cuts::ptIn(20*GeV, 10000.0*GeV) && Cuts::absrap < 4.7); //jet sorting by pT
	
		
		// calculate delta_phi
		if ((jets.size() > 0) && (zfinder.bosons()[0].momentum().pT() > 30) ) {
			//const double deltaphi = deltaPhi(zfinder.bosons()[0], jets[0]);
			

//			const double deltaphi = fabs(zfinder.bosons()[0].momentum().phi()-jets[0].momentum().phi());
//			_h_deltaphi->fill(deltaphi, weight);	
//			_h_njets->fill(jets.size(), weight);

			
		
		}




///		///konstituenten, aus denen Z rekonstruiert wurde

		      const ParticleVector& leptons = zfinder.constituents();
		      if(!((leptons[0].pT()>27 && leptons[1].pT()>20) || (leptons[1].pT()>27 && leptons[0].pT()>20))) vetoEvent;
		      if (leptons.size() != 2 || leptons[0].threeCharge() * leptons[1].threeCharge() > 0) vetoEvent;
		      const Particle& lminus = leptons[0].charge() < 0 ? leptons[0] : leptons[1];
		      const Particle& lplus  = leptons[0].charge() < 0 ? leptons[1] : leptons[0];




///		///phi_star berechnen
		      const double phi_acop = M_PI - deltaPhi(lminus, lplus);
		      const double costhetastar = tanh( 0.5 * (lminus.eta() - lplus.eta()) );
		      const double sin2thetastar = (costhetastar > 1) ? 0.0 : (1.0 - sqr(costhetastar));
		      const double phistar = tan(0.5 * phi_acop) * sqrt(sin2thetastar);






			// muon histos

///		///aendere, dass muplus und muminus beruecksichtigt
			
//				_h_pTmu->fill(lminus.pt(), weight);
//				_h_pTmu->fill(lplus.pt(), weight);
//				_h_etamu->fill(lminus.eta(), weight);
//				_h_etamu->fill(lplus.eta(), weight);
//				_h_phimu->fill(lminus.phi()-pi, weight);
//				_h_phimu->fill(lplus.phi()-pi, weight);
			
				// Z histos
				_h_pTZ->fill(pTZ, weight);
//				_h_yZ->fill(yZ, weight);
				_h_absyZ->fill(fabs(yZ), weight);
//				_h_mZ->fill(mZ, weight);
//				_h_phiZ->fill(phiZ, weight);


///			//phistar histogramme fuer den betrachteten Bereich (81 bis 111 GeV)
				_h_phistar->fill(phistar, weight);
	        		



				// Z pT in y bins
				if (std::abs(yZ) < m_ybins[0]){
					_h_pTZ_0->fill(pTZ, weight);
					_fnlo_pTZ_0->fill(pTZ, event);
					_h_phistar_0->fill(phistar, weight);
                                        _fnlo_phistar_0->fill(phistar, event); 
				}
				else if (std::abs(yZ) < m_ybins[1]){
					_h_pTZ_1->fill(pTZ, weight);
					_fnlo_pTZ_1->fill(pTZ, event);
					_h_phistar_1->fill(phistar, weight);
                                        _fnlo_phistar_1->fill(phistar, event);
				}
				else if (std::abs(yZ) < m_ybins[2]){
					_h_pTZ_2->fill(pTZ, weight);
					_fnlo_pTZ_2->fill(pTZ, event);
					_h_phistar_2->fill(phistar, weight);
                                        _fnlo_phistar_2->fill(phistar, event);
				}
				else if (std::abs(yZ) < m_ybins[3]){
					_h_pTZ_3->fill(pTZ, weight);
					_fnlo_pTZ_3->fill(pTZ, event);
					_h_phistar_3->fill(phistar, weight);
                                        _fnlo_phistar_3->fill(phistar, event);
				}
				else if (std::abs(yZ) < m_ybins[4]){
                                        _h_pTZ_4->fill(pTZ, weight);
                                         _fnlo_pTZ_4->fill(pTZ, event);
					_h_phistar_4->fill(phistar, weight);
                                        _fnlo_phistar_4->fill(phistar, event);
                                }
				else if (std::abs(yZ) < m_ybins[5]){
                                        _h_pTZ_5->fill(pTZ, weight);
                                        _fnlo_pTZ_5->fill(pTZ, event);
					_h_phistar_5->fill(phistar, weight);
                                        _fnlo_phistar_5->fill(phistar, event);
                                }


				

				_fnlo_pTZ->fill(pTZ, event);
//				_fnlo_yZ->fill(yZ, event);
				_fnlo_absyZ->fill(fabs(yZ), event);
//				_fnlo_mZ->fill(mZ, event);
				_fnlo_phistar->fill(phistar, event);

		}
		else {
			MSG_DEBUG("no unique lepton pair found: " << zfinder.bosons().size() << " weight: " << weight);
		}

	}


	/// Normalise histograms etc., after the run
	void finalize() {

		double normfactor = crossSection()/sumOfWeights();

		// scale rivet
//		scale(_h_yZ, normfactor);
		scale(_h_absyZ, normfactor);
		scale(_h_pTZ, normfactor);
//		scale(_h_mZ, normfactor);
//		scale(_h_phiZ, normfactor);
		
		scale(_h_pTZ_0, normfactor);
		scale(_h_pTZ_1, normfactor);
		scale(_h_pTZ_2, normfactor);
		scale(_h_pTZ_3, normfactor);
		scale(_h_pTZ_4, normfactor);
		scale(_h_pTZ_5, normfactor);


//		scale(_h_pTmu, normfactor);
//		scale(_h_etamu, normfactor);
//		scale(_h_phimu, normfactor);

///		skalierung rivet phistar
		scale(_h_phistar, normfactor);
		
		scale(_h_phistar_0, normfactor);
                scale(_h_phistar_1, normfactor);
                scale(_h_phistar_2, normfactor);
                scale(_h_phistar_3, normfactor);
                scale(_h_phistar_4, normfactor);
                scale(_h_phistar_5, normfactor);

		//scale rivet deltaphi(jet, Z)
//		scale(_h_deltaphi, normfactor);
		//scale(_h_njets, normfactor);

		//scale fastnlo
		_fnlo_pTZ->scale(normfactor);
//		_fnlo_yZ->scale(normfactor);
		_fnlo_absyZ->scale(normfactor);
//		_fnlo_mZ->scale(normfactor);

		_fnlo_pTZ_0->scale(normfactor);
		_fnlo_pTZ_1->scale(normfactor);
		_fnlo_pTZ_2->scale(normfactor);
		_fnlo_pTZ_3->scale(normfactor);
		_fnlo_pTZ_4->scale(normfactor);
		_fnlo_pTZ_5->scale(normfactor);

///		skalierung fastnlo phistar
		_fnlo_phistar->scale(normfactor);
			
		_fnlo_phistar_0->scale(normfactor);
                _fnlo_phistar_1->scale(normfactor);
                _fnlo_phistar_2->scale(normfactor);
                _fnlo_phistar_3->scale(normfactor);
                _fnlo_phistar_4->scale(normfactor);
                _fnlo_phistar_5->scale(normfactor);
			

		_fnlo_pTZ->exportgrid();
//		_fnlo_yZ->exportgrid();
		_fnlo_absyZ->exportgrid();
//		_fnlo_mZ->exportgrid();

		_fnlo_pTZ_0->exportgrid();
		_fnlo_pTZ_1->exportgrid();
		_fnlo_pTZ_2->exportgrid();
		_fnlo_pTZ_3->exportgrid();
		_fnlo_pTZ_4->exportgrid();
		_fnlo_pTZ_5->exportgrid();
		

///		exportieren fastnlo phistar
		_fnlo_phistar->exportgrid();

		_fnlo_phistar_0->exportgrid();
                _fnlo_phistar_1->exportgrid();
                _fnlo_phistar_2->exportgrid();
                _fnlo_phistar_3->exportgrid();
                _fnlo_phistar_4->exportgrid();
                _fnlo_phistar_5->exportgrid();

		// Clear event handler
		MCgrid::PDFHandler::CheckOutAnalysis(histoDir());
	}

private:

	std::vector<double> m_ybins;
	std::vector<double> yb_bins;

	/// Histograms
	Histo1DPtr _h_pTZ;
//	Histo1DPtr _h_yZ;
	Histo1DPtr _h_absyZ;
//	Histo1DPtr _h_mZ;
	Histo1DPtr _h_phiZ;

//	Histo1DPtr _h_pTmu;
//	Histo1DPtr _h_etamu;
//	Histo1DPtr _h_phimu;

	// for deltaphi
//	Histo1DPtr _h_deltaphi;
//	Histo1DPtr _h_njets;

///	fuer phistar
	Histo1DPtr _h_phistar;



	// pT in y bins
	Histo1DPtr _h_pTZ_0;
	Histo1DPtr _h_pTZ_1;
	Histo1DPtr _h_pTZ_2;
	Histo1DPtr _h_pTZ_3;
	Histo1DPtr _h_pTZ_4;
	Histo1DPtr _h_pTZ_5;

  	Histo1DPtr _h_phistar_0;
        Histo1DPtr _h_phistar_1;
        Histo1DPtr _h_phistar_2;
        Histo1DPtr _h_phistar_3;
        Histo1DPtr _h_phistar_4;
        Histo1DPtr _h_phistar_5;


	// fastNLO (MCgrid) grids
	MCgrid::gridPtr _fnlo_pTZ;
//	MCgrid::gridPtr _fnlo_yZ;
	MCgrid::gridPtr _fnlo_absyZ;
//	MCgrid::gridPtr _fnlo_mZ;

///	fuer phistar
	MCgrid::gridPtr _fnlo_phistar;

	
	MCgrid::gridPtr _fnlo_pTZ_0;
	MCgrid::gridPtr _fnlo_pTZ_1;
	MCgrid::gridPtr _fnlo_pTZ_2;
	MCgrid::gridPtr _fnlo_pTZ_3;
	MCgrid::gridPtr _fnlo_pTZ_4;
	MCgrid::gridPtr _fnlo_pTZ_5;

	MCgrid::gridPtr _fnlo_phistar_0;
        MCgrid::gridPtr _fnlo_phistar_1;
        MCgrid::gridPtr _fnlo_phistar_2;
        MCgrid::gridPtr _fnlo_phistar_3;
        MCgrid::gridPtr _fnlo_phistar_4;
        MCgrid::gridPtr _fnlo_phistar_5;
};


// The hook for the plugin system
DECLARE_RIVET_PLUGIN(MCgrid_CMS_2015_Zee);
}
