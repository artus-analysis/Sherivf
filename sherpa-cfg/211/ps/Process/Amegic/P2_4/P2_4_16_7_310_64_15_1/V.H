//Header file for process VP2_4_16_7_310_64_15_1

#ifndef VP2_4_16_7_310_64_15_1_on
#define VP2_4_16_7_310_64_15_1_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_4_16_7_310_64_15_1(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_4_16_7_310_64_15_1 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_4_16_7_310_64_15_1(Basic_Sfuncs* _BS);
  ~VP2_4_16_7_310_64_15_1();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_1();
  void Calculate_2();
  void Calculate_M0();
  void Calculate_M1();
  void Calculate_M2();
  void Calculate_M3();
  void Calculate_M12();
  void Calculate_M13();
  void Calculate_M14();
  void Calculate_M15();
  void Calculate_M16();
  void Calculate_M17();
  void Calculate_M28();
  void Calculate_M29();
  void Calculate_M34();
  void Calculate_M35();
  void Calculate_M46();
  void Calculate_M47();
  void Calculate_M48();
  void Calculate_M49();
  void Calculate_M50();
  void Calculate_M51();
  void Calculate_M60();
  void Calculate_M61();
  void Calculate_M62();
  void Calculate_M63();
};
}

#endif
