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
    MCgrid_CMS_2015_Zee()
      : Analysis("MCgrid_CMS_2015_Zee")
    {    }

  public:

    /// Book histograms and initialise projections before the run
    void init() {

      /// Initialise and register projections here
      // this seems to have been corrected completely for all selection cuts,
      // i.e. eta cuts and pT cuts on leptons.
      Cut cut = (
          (Cuts::pT >= 25.0*GeV) &
          (Cuts::etaIn(-2.4, -1.566) | Cuts::etaIn(-1.442, 1.442) | Cuts::etaIn(1.566, 2.4))
      );

      ZFinder zfinder(FinalState(), cut, PID::ELECTRON,
                      81*GeV, 101*GeV, 0.2,
                       ZFinder::CLUSTERNODECAY, ZFinder::TRACK);
      addProjection(zfinder, "ZFinder");
      
      // electrons
      IdentifiedFinalState electrons;
      electrons.acceptId(PID::ELECTRON);
      addProjection(electrons, "Electrons");
      
      /// Book histograms here
      _h_pTZ = bookHisto1D("d01-x01-y01", 37, 30, 400);
      _h_yZ = bookHisto1D("d02-x01-y01", 25, 0, 2.5);
      _h_mZ = bookHisto1D("d03-x01-y01", 20, 81, 101);
      _h_phiZ = bookHisto1D("d04-x01-y01", 20, -3.14159, 3.14159);
      
      _pTZ_yZ = bookProfile1D("d05-x01-y01", 25, 0, 2.5);
      _yZ_pTZ = bookProfile1D("d06-x01-y01", 37, 30, 400);
      
      
      _h_pTe = bookHisto1D("d07-x01-y01", 40, 0, 200);
      _h_etae = bookHisto1D("d08-x01-y01", 60, -3, 3);
      _h_phie = bookHisto1D("d10-x01-y01", 20, -3.14159, 3.14159);

#if USE_FNLO
      MSG_INFO("Using fastnlo");
      const string steeringFileName = "MCgrid_CMS_2015_Zee.str";
      const string steeringFileName2 = "MCgrid_CMS_2015_Zee_2.str";
      const string steeringFileName3 = "MCgrid_CMS_2015_Zee_3.str";
      const string steeringFileName4 = "MCgrid_CMS_2015_Zee_4.str";

      MSG_INFO("Creating fastnloGridArch and fastnloConfig");
      MCgrid::fastnloGridArch arch_fnlo(50, 1, "Lagrange", "OneNode", "sqrtlog10", "linear");
      MCgrid::fastnloConfig config_fnlo(0, 8000.0, MCgrid::BEAM_PROTON, MCgrid::BEAM_PROTON, steeringFileName, arch_fnlo);
      MCgrid::fastnloConfig config_fnlo_2(0, 8000.0, MCgrid::BEAM_PROTON, MCgrid::BEAM_PROTON, steeringFileName2, arch_fnlo);
      MCgrid::fastnloConfig config_fnlo_3(0, 8000.0, MCgrid::BEAM_PROTON, MCgrid::BEAM_PROTON, steeringFileName3, arch_fnlo);
      MCgrid::fastnloConfig config_fnlo_4(0, 8000.0, MCgrid::BEAM_PROTON, MCgrid::BEAM_PROTON, steeringFileName4, arch_fnlo);

      MSG_INFO("bookGrid for yZ. histoDir: " << histoDir());
      _fnlo_pTZ = MCgrid::bookGrid(_h_pTZ, histoDir(), config_fnlo, "fnlo_pTZ_warmup.txt");
      _fnlo_yZ = MCgrid::bookGrid(_h_yZ, histoDir(), config_fnlo_2, "fnlo_yZ_warmup.txt");
      _fnlo_mZ = MCgrid::bookGrid(_h_mZ, histoDir(), config_fnlo_3, "fnlo_mZ_warmup.txt");
      _fnlo_phiZ = MCgrid::bookGrid(_h_phiZ, histoDir(), config_fnlo_4, "fnlo_phiZ_warmup.txt");

      //_fnlo_xs = MCgrid::bookGrid(_h_xs, histoDir(), config_fnlo);

      MSG_INFO("fastnlo init done");
#endif
    }


    /// Perform the per-event analysis
    void analyze(const Event& event) {
      
      // Handle APPL event
      MCgrid::PDFHandler::HandleEvent(event);
      
      const double weight = event.weight();

      const ZFinder& zfinder = applyProjection<ZFinder>(event, "ZFinder");
      if (zfinder.bosons().size() == 1) {
        double yZ = fabs(zfinder.bosons()[0].momentum().rapidity());
        double pTZ = zfinder.bosons()[0].momentum().pT();
        double mZ = zfinder.bosons()[0].momentum().mass();
        double phiZ = zfinder.bosons()[0].momentum().phi()-pi;

        if (pTZ > 30.)
        {
             // electron histos
             const Particles particles = applyProjection<FinalState>(event, "Electrons").particlesByPt(Cuts::pT>=0.5*GeV);
             _h_pTe->fill(particles[0].pt(), weight);
             _h_etae->fill(particles[0].eta(), weight);
             _h_phie->fill(particles[0].phi()-pi, weight);

             // Z histos
             _h_pTZ->fill(pTZ, weight);
             _h_yZ->fill(yZ, weight);
             _h_mZ->fill(mZ, weight);
             _h_phiZ->fill(phiZ, weight);

             _pTZ_yZ->fill(yZ, pTZ, weight);
             _yZ_pTZ->fill(pTZ, yZ, weight);

#if USE_FNLO
            _fnlo_yZ->fill(yZ, event);
            _fnlo_pTZ->fill(pTZ, event);
            _fnlo_mZ->fill(mZ, event);
            _fnlo_phiZ->fill(phiZ, event);
#endif
        }
      }
      else {
        MSG_DEBUG("no unique lepton pair found.");
      }

    }


    /// Normalise histograms etc., after the run
    void finalize() {

      // Data seems to have been normalized for the avg of the two sides
      // (+ve & -ve rapidity) rather than the sum, hence the 0.5:
      scale(_h_yZ, crossSection()/sumOfWeights());
      //scale(_h_yZ, 0.5*crossSection()/sumOfWeights());
      scale(_h_pTZ, crossSection()/sumOfWeights());
      scale(_h_mZ, crossSection()/sumOfWeights());
      scale(_h_phiZ, crossSection()/sumOfWeights());

      scale(_h_pTe, crossSection()/sumOfWeights());
      scale(_h_etae, crossSection()/sumOfWeights());
      scale(_h_phie, crossSection()/sumOfWeights());

#if USE_FNLO
      _fnlo_pTZ->scale(crossSection()/sumOfWeights());
      //_fnlo_yZ->scale(0.5*crossSection()/sumOfWeights());
      _fnlo_yZ->scale(crossSection()/sumOfWeights());
      _fnlo_mZ->scale(crossSection()/sumOfWeights());
      _fnlo_phiZ->scale(crossSection()/sumOfWeights());

      _fnlo_pTZ->exportgrid("fnlo_pTZ.txt");
      _fnlo_yZ->exportgrid("fnlo_yZ.txt");
      _fnlo_mZ->exportgrid("fnlo_mZ.txt");
      _fnlo_phiZ->exportgrid("fnlo_phiZ.txt");
#endif
      
      // Clear event handler
      MCgrid::PDFHandler::ClearHandler();
    }


  private:

    /// @name Histograms
    Histo1DPtr _h_pTZ;
    Histo1DPtr _h_yZ;
    Histo1DPtr _h_mZ;
    Histo1DPtr _h_phiZ;
    //Histo1DPtr _h_xs;
    Profile1DPtr _pTZ_yZ;
    Profile1DPtr _yZ_pTZ;
    
    Histo1DPtr _h_pTe;
    Histo1DPtr _h_etae;
    Histo1DPtr _h_phie;
    
    // Grids
#if USE_FNLO
    MCgrid::gridPtr _fnlo_pTZ;
    MCgrid::gridPtr _fnlo_yZ;
    MCgrid::gridPtr _fnlo_mZ;
    MCgrid::gridPtr _fnlo_phiZ;
    //MCgrid::gridPtr _fnlo_xs;
#endif

  };


  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(MCgrid_CMS_2015_Zee);

}
