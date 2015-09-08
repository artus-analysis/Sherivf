//Header file for process VP2_4_8_10_174_64_13_1

#ifndef VP2_4_8_10_174_64_13_1_on
#define VP2_4_8_10_174_64_13_1_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_4_8_10_174_64_13_1(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_4_8_10_174_64_13_1 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_4_8_10_174_64_13_1(Basic_Sfuncs* _BS);
  ~VP2_4_8_10_174_64_13_1();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M12();
  void Calculate_M17();
  void Calculate_M29();
  void Calculate_M34();
  void Calculate_M46();
  void Calculate_M51();
  void Calculate_M63();
};
}

#endif
