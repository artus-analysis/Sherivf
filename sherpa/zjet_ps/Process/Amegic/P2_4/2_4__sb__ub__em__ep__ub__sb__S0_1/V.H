//Header file for process V2_4__sb__ub__em__ep__ub__sb__S0_1

#ifndef V2_4__sb__ub__em__ep__ub__sb__S0_1_on
#define V2_4__sb__ub__em__ep__ub__sb__S0_1_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__sb__ub__em__ep__ub__sb__S0_1(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__sb__ub__em__ep__ub__sb__S0_1 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__sb__ub__em__ep__ub__sb__S0_1(Basic_Sfuncs* _BS);
  ~V2_4__sb__ub__em__ep__ub__sb__S0_1();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
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
  void Calculate_M32();
  void Calculate_M33();
  void Calculate_M44();
  void Calculate_M45();
  void Calculate_M50();
  void Calculate_M51();
  void Calculate_M62();
  void Calculate_M63();
};
}

#endif
