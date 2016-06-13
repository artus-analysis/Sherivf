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

		// muon cuts
		Cut cut = (
			(Cuts::pT >= 20.*GeV)
			& (Cuts::etaIn(-2.3, 2.3))
		);
		// Z boson reconstruction
		ZFinder zfinder(FinalState(), cut, PID::MUON, 81*GeV, 111*GeV, 0.2, ZFinder::CLUSTERNODECAY, ZFinder::TRACK);
		// register projections here
		addProjection(zfinder, "ZFinder");
		IdentifiedFinalState muons;
		muons.acceptId(PID::MUON);
		addProjection(muons, "Muons");

		/// Book RIVET histograms
		std::vector<double> bin_edges = {30, 40, 50, 60, 80, 100, 120, 140, 170, 200, 1000};
		m_ybins = {0.4, 0.8, 1.2, 1.6, 2.0, 2.4};
		_h_pTZ = bookHisto1D("zpt", bin_edges);
		_h_yZ = bookHisto1D("zy", 48, -2.4, 2.4);
		_h_absyZ = bookHisto1D("abszy", 24, 0, 2.4);
		_h_mZ = bookHisto1D("zmass", 20, 81, 101);
		_h_phiZ = bookHisto1D("zphi", 32, -3.2, 3.2);

		_h_pTmu = bookHisto1D("muminuspt", 20, 20, 120);
		_h_etamu = bookHisto1D("muminuseta", 48, -2.4, 2.4);
		_h_phimu = bookHisto1D("muminusphi", 32, -3.2, 3.2);

		_h_pTZ_0 = bookHisto1D("y0_zpt", bin_edges);
		_h_pTZ_1 = bookHisto1D("y1_zpt", bin_edges);
		_h_pTZ_2 = bookHisto1D("y2_zpt", bin_edges);
		_h_pTZ_3 = bookHisto1D("y3_zpt", bin_edges);
		_h_pTZ_4 = bookHisto1D("y4_zpt", bin_edges);
		_h_pTZ_5 = bookHisto1D("y5_zpt", bin_edges);


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
		// in bins
		MCgrid::fastnloConfig config_fnlo_4(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_5(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_6(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_7(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_8(1, subproc, arch_fnlo, center_of_mass_energy);
		MCgrid::fastnloConfig config_fnlo_9(1, subproc, arch_fnlo, center_of_mass_energy);

		MSG_INFO("bookGrid. histoDir: " << histoDir());
		_fnlo_pTZ = MCgrid::bookGrid(_h_pTZ, histoDir(), config_fnlo);
		_fnlo_absyZ = MCgrid::bookGrid(_h_absyZ, histoDir(), config_fnlo_1);
		_fnlo_yZ = MCgrid::bookGrid(_h_yZ, histoDir(), config_fnlo_2);
		_fnlo_mZ = MCgrid::bookGrid(_h_mZ, histoDir(), config_fnlo_3);

		_fnlo_pTZ_0 = MCgrid::bookGrid(_h_pTZ_0, histoDir(), config_fnlo_4);
		_fnlo_pTZ_1 = MCgrid::bookGrid(_h_pTZ_1, histoDir(), config_fnlo_5);
		_fnlo_pTZ_2 = MCgrid::bookGrid(_h_pTZ_2, histoDir(), config_fnlo_6);
		_fnlo_pTZ_3 = MCgrid::bookGrid(_h_pTZ_3, histoDir(), config_fnlo_7);
		_fnlo_pTZ_4 = MCgrid::bookGrid(_h_pTZ_4, histoDir(), config_fnlo_8);
		_fnlo_pTZ_5 = MCgrid::bookGrid(_h_pTZ_5, histoDir(), config_fnlo_9);
		MSG_INFO("fastnlo init done");
	}


	/// Perform the per-event analysis
	void analyze(const Event& event) {

		// Handle event
		MCgrid::PDFHandler::HandleEvent(event, histoDir());
		const double weight = event.weight();
		const Particles particles = applyProjection<FinalState>(event, "Muons").particlesByPt(Cuts::pT>=0.5*GeV);
		const ZFinder& zfinder = applyProjection<ZFinder>(event, "ZFinder");

		if (zfinder.bosons().size() == 1) {

			double yZ = zfinder.bosons()[0].momentum().rapidity();
			double pTZ = zfinder.bosons()[0].momentum().pT();
			double mZ = zfinder.bosons()[0].momentum().mass();
			double phiZ = zfinder.bosons()[0].momentum().phi()-pi;

			// muon histos
			if (particles.size() > 0)
			{
				_h_pTmu->fill(particles[0].pt(), weight);
				_h_etamu->fill(particles[0].eta(), weight);
				_h_phimu->fill(particles[0].phi()-pi, weight);
			}
				// Z histos
				_h_pTZ->fill(pTZ, weight);
				_h_yZ->fill(yZ, weight);
				_h_absyZ->fill(fabs(yZ), weight);
				_h_mZ->fill(mZ, weight);
				_h_phiZ->fill(phiZ, weight);

				// Z pT in y bins
				if (std::abs(yZ) < m_ybins[0]){
					_h_pTZ_0->fill(pTZ, weight);
						_fnlo_pTZ_0->fill(pTZ, event);
				}
				else if (std::abs(yZ) < m_ybins[1]){
					_h_pTZ_1->fill(pTZ, weight);
						_fnlo_pTZ_1->fill(pTZ, event);
				}
				else if (std::abs(yZ) < m_ybins[2]){
					_h_pTZ_2->fill(pTZ, weight);
						_fnlo_pTZ_2->fill(pTZ, event);
				}
				else if (std::abs(yZ) < m_ybins[3]){
					_h_pTZ_3->fill(pTZ, weight);
						_fnlo_pTZ_3->fill(pTZ, event);
				}
				else if (std::abs(yZ) < m_ybins[4]){
					_h_pTZ_4->fill(pTZ, weight);
						_fnlo_pTZ_4->fill(pTZ, event);
				}
				else if (std::abs(yZ) < m_ybins[5]){
					_h_pTZ_5->fill(pTZ, weight);
						_fnlo_pTZ_5->fill(pTZ, event);
				}
				_fnlo_pTZ->fill(pTZ, event);
				_fnlo_yZ->fill(yZ, event);
				_fnlo_absyZ->fill(fabs(yZ), event);
				_fnlo_mZ->fill(mZ, event);

		}
		else {
			MSG_DEBUG("no unique lepton pair found: " << zfinder.bosons().size() << " weight: " << weight);
		}

	}


	/// Normalise histograms etc., after the run
	void finalize() {

		double normfactor = crossSection()/sumOfWeights();

		// scale rivet
		scale(_h_yZ, normfactor);
		scale(_h_absyZ, normfactor);
		scale(_h_pTZ, normfactor);
		scale(_h_mZ, normfactor);
		scale(_h_phiZ, normfactor);
		
		scale(_h_pTZ_0, normfactor);
		scale(_h_pTZ_1, normfactor);
		scale(_h_pTZ_2, normfactor);
		scale(_h_pTZ_3, normfactor);
		scale(_h_pTZ_4, normfactor);
		scale(_h_pTZ_5, normfactor);

		scale(_h_pTmu, normfactor);
		scale(_h_etamu, normfactor);
		scale(_h_phimu, normfactor);

		//scale fastnlo
		_fnlo_pTZ->scale(normfactor);
		_fnlo_yZ->scale(normfactor);
		_fnlo_absyZ->scale(normfactor);
		_fnlo_mZ->scale(normfactor);

		_fnlo_pTZ_0->scale(normfactor);
		_fnlo_pTZ_1->scale(normfactor);
		_fnlo_pTZ_2->scale(normfactor);
		_fnlo_pTZ_3->scale(normfactor);
		_fnlo_pTZ_4->scale(normfactor);
		_fnlo_pTZ_5->scale(normfactor);

		_fnlo_pTZ->exportgrid();
		_fnlo_yZ->exportgrid();
		_fnlo_absyZ->exportgrid();
		_fnlo_mZ->exportgrid();

		_fnlo_pTZ_0->exportgrid();
		_fnlo_pTZ_1->exportgrid();
		_fnlo_pTZ_2->exportgrid();
		_fnlo_pTZ_3->exportgrid();
		_fnlo_pTZ_4->exportgrid();
		_fnlo_pTZ_5->exportgrid();

		// Clear event handler
		MCgrid::PDFHandler::CheckOutAnalysis(histoDir());
	}

private:

	std::vector<double> m_ybins;

	/// Histograms
	Histo1DPtr _h_pTZ;
	Histo1DPtr _h_yZ;
	Histo1DPtr _h_absyZ;
	Histo1DPtr _h_mZ;
	Histo1DPtr _h_phiZ;

	Histo1DPtr _h_pTmu;
	Histo1DPtr _h_etamu;
	Histo1DPtr _h_phimu;

	// pT in y bins
	Histo1DPtr _h_pTZ_0;
	Histo1DPtr _h_pTZ_1;
	Histo1DPtr _h_pTZ_2;
	Histo1DPtr _h_pTZ_3;
	Histo1DPtr _h_pTZ_4;
	Histo1DPtr _h_pTZ_5;

	// fastNLO (MCgrid) grids
	MCgrid::gridPtr _fnlo_pTZ;
	MCgrid::gridPtr _fnlo_yZ;
	MCgrid::gridPtr _fnlo_absyZ;
	MCgrid::gridPtr _fnlo_mZ;
	
	MCgrid::gridPtr _fnlo_pTZ_0;
	MCgrid::gridPtr _fnlo_pTZ_1;
	MCgrid::gridPtr _fnlo_pTZ_2;
	MCgrid::gridPtr _fnlo_pTZ_3;
	MCgrid::gridPtr _fnlo_pTZ_4;
	MCgrid::gridPtr _fnlo_pTZ_5;
};


// The hook for the plugin system
DECLARE_RIVET_PLUGIN(MCgrid_CMS_2015_Zee);
}
