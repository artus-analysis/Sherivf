//Header file for process VP2_4_16_10_364_64_18_0

#ifndef VP2_4_16_10_364_64_18_0_on
#define VP2_4_16_10_364_64_18_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_4_16_10_364_64_18_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_4_16_10_364_64_18_0 : public Values,
  public Basic_Zfunc,
  public Basic_Xfunc,
  public Basic_Vfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_4_16_10_364_64_18_0(Basic_Sfuncs* _BS);
  ~VP2_4_16_10_364_64_18_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_1();
  void Calculate_2();
  void Calculate_M0();
  void Calculate_M2();
  void Calculate_M12();
  void Calculate_M14();
  void Calculate_M16();
  void Calculate_M18();
  void Calculate_M28();
  void Calculate_M30();
  void Calculate_M33();
  void Calculate_M35();
  void Calculate_M45();
  void Calculate_M47();
  void Calculate_M49();
  void Calculate_M51();
  void Calculate_M61();
  void Calculate_M63();
};
}

#endif
