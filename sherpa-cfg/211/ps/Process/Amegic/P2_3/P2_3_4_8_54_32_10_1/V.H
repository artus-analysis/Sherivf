//Header file for process VP2_3_4_8_54_32_10_1

#ifndef VP2_3_4_8_54_32_10_1_on
#define VP2_3_4_8_54_32_10_1_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_3_4_8_54_32_10_1(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_3_4_8_54_32_10_1 : public Values,
  public Basic_Zfunc,
  public Basic_Xfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_3_4_8_54_32_10_1(Basic_Sfuncs* _BS);
  ~VP2_3_4_8_54_32_10_1();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 8; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M2();
  void Calculate_M12();
  void Calculate_M14();
  void Calculate_M17();
  void Calculate_M19();
  void Calculate_M29();
  void Calculate_M31();
};
}

#endif
