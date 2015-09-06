//Header file for process VP2_4_8_7_244_64_13_10

#ifndef VP2_4_8_7_244_64_13_10_on
#define VP2_4_8_7_244_64_13_10_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_4_8_7_244_64_13_10(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_4_8_7_244_64_13_10 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_4_8_7_244_64_13_10(Basic_Sfuncs* _BS);
  ~VP2_4_8_7_244_64_13_10();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M1();
  void Calculate_M12();
  void Calculate_M13();
  void Calculate_M16();
  void Calculate_M17();
  void Calculate_M28();
  void Calculate_M29();
  void Calculate_M34();
  void Calculate_M35();
  void Calculate_M46();
  void Calculate_M47();
  void Calculate_M50();
  void Calculate_M51();
  void Calculate_M62();
  void Calculate_M63();
};
}

#endif
