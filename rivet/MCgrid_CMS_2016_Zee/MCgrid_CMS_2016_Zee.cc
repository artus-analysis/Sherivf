// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Cuts.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/ZFinder.hh"

#include "Rivet/Projections/IdentifiedFinalState.hh"

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

		/// Initialise and register projections here
		Cut cut = (
			#if USE_MUONS
			(Cuts::pT >= 20.*GeV) &
			(Cuts::etaIn(-2.3, 2.3))
			#else
			(Cuts::pT >= 25.*GeV)
			& (Cuts::etaIn(-2.4, -1.566) | Cuts::etaIn(-1.442, 1.442) | Cuts::etaIn(1.566, 2.4))
			#endif
		);

		ZFinder zfinder(FinalState(), cut,
			#if USE_MUONS
			PID::MUON,
			#else
			PID::ELECTRON,
			#endif
			81*GeV, 111*GeV, 0.2, ZFinder::CLUSTERNODECAY, ZFinder::TRACK);
		addProjection(zfinder, "ZFinder");

		// electrons
		IdentifiedFinalState electrons;
		electrons.acceptId(PID::ELECTRON);
		addProjection(electrons, "Electrons");

		/// Book histograms here
		std::vector<double> bin_edges = {30, 40, 50, 60, 80, 100, 120, 140, 170, 200, 1000};
		m_ybins = {0.4, 0.8, 1.2, 1.6, 2.0, 2.4};
		_h_pTZ = bookHisto1D("zpt", bin_edges);
		_h_yZ = bookHisto1D("abszy", 24, 0, 2.4);
		_h_mZ = bookHisto1D("zmass", 20, 81, 101);
		_h_phiZ = bookHisto1D("zphi", 32, -3.2, 3.2);

		_h_pTe = bookHisto1D("eminuspt", 20, 20, 120);
		_h_etae = bookHisto1D("eminuseta", 48, -2.4, 2.4);
		_h_phie = bookHisto1D("eminusphi", 32, -3.2, 3.2);
	}


	/// Perform the per-event analysis
	void analyze(const Event& event) {

		// Handle event
		MCgrid::PDFHandler::HandleEvent(event, histoDir());
		const double weight = event.weight();
		const Particles particles = applyProjection<FinalState>(event, "Electrons").particlesByPt(Cuts::pT>=0.5*GeV);
		const ZFinder& zfinder = applyProjection<ZFinder>(event, "ZFinder");

		if (zfinder.bosons().size() == 1) {

			double yZ = fabs(zfinder.bosons()[0].momentum().rapidity());
			double pTZ = zfinder.bosons()[0].momentum().pT();
			double mZ = zfinder.bosons()[0].momentum().mass();
			double phiZ = zfinder.bosons()[0].momentum().phi()-pi;

			// electron histos
			if (particles.size() > 0)
			{
				_h_pTe->fill(particles[0].pt(), weight);
				_h_etae->fill(particles[0].eta(), weight);
				_h_phie->fill(particles[0].phi()-pi, weight);
			}
				// Z histos
				_h_pTZ->fill(pTZ, weight);
				_h_yZ->fill(yZ, weight);
				_h_mZ->fill(mZ, weight);
				_h_phiZ->fill(phiZ, weight);

		}
		else {
			MSG_DEBUG("no unique lepton pair found: " << zfinder.bosons().size() << " weight: " << weight);
		}

	}


	/// Normalise histograms etc., after the run
	void finalize() {

		double normfactor = crossSection()/sumOfWeights();
		MSG_INFO("xsec: " << crossSection() << " sumW: " << sumOfWeights() << " ratio: " << crossSection()/sumOfWeights());

		// scale rivet
		scale(_h_yZ, normfactor);
		scale(_h_pTZ, normfactor);
		scale(_h_mZ, normfactor);
		scale(_h_phiZ, normfactor);
		
		scale(_h_pTe, normfactor);
		scale(_h_etae, normfactor);
		scale(_h_phie, normfactor);


		// Clear event handler
		MCgrid::PDFHandler::CheckOutAnalysis(histoDir());
	}

private:

	std::vector<double> m_ybins;

	/// Histograms
	Histo1DPtr _h_pTZ;
	Histo1DPtr _h_yZ;
	Histo1DPtr _h_mZ;
	Histo1DPtr _h_phiZ;

	Histo1DPtr _h_pTe;
	Histo1DPtr _h_etae;
	Histo1DPtr _h_phie;
};

// The hook for the plugin system
DECLARE_RIVET_PLUGIN(MCgrid_CMS_2015_Zee);
}
