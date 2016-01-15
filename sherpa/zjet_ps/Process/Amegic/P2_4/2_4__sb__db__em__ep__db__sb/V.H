//Header file for process V2_4__sb__db__em__ep__db__sb

#ifndef V2_4__sb__db__em__ep__db__sb_on
#define V2_4__sb__db__em__ep__db__sb_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__sb__db__em__ep__db__sb(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__sb__db__em__ep__db__sb : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__sb__db__em__ep__db__sb(Basic_Sfuncs* _BS);
  ~V2_4__sb__db__em__ep__db__sb();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
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
