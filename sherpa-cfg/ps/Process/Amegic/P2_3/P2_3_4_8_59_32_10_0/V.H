//Header file for process VP2_3_4_8_59_32_10_0

#ifndef VP2_3_4_8_59_32_10_0_on
#define VP2_3_4_8_59_32_10_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_3_4_8_59_32_10_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_3_4_8_59_32_10_0 : public Values,
  public Basic_Zfunc,
  public Basic_Xfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_3_4_8_59_32_10_0(Basic_Sfuncs* _BS);
  ~VP2_3_4_8_59_32_10_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 8; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M1();
  void Calculate_M12();
  void Calculate_M13();
  void Calculate_M18();
  void Calculate_M19();
  void Calculate_M30();
  void Calculate_M31();
};
}

#endif
