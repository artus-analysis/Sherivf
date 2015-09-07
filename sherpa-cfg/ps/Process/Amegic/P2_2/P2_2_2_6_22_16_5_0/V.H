//Header file for process VP2_2_2_6_22_16_5_0

#ifndef VP2_2_2_6_22_16_5_0_on
#define VP2_2_2_6_22_16_5_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_2_2_6_22_16_5_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_2_2_6_22_16_5_0 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_2_2_6_22_16_5_0(Basic_Sfuncs* _BS);
  ~VP2_2_2_6_22_16_5_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 6; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M1();
  void Calculate_M2();
  void Calculate_M3();
  void Calculate_M12();
  void Calculate_M13();
  void Calculate_M14();
  void Calculate_M15();
};
}

#endif
