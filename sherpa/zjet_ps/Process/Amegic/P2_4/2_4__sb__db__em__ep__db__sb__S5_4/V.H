//Header file for process V2_4__sb__db__em__ep__db__sb__S5_4

#ifndef V2_4__sb__db__em__ep__db__sb__S5_4_on
#define V2_4__sb__db__em__ep__db__sb__S5_4_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__sb__db__em__ep__db__sb__S5_4(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__sb__db__em__ep__db__sb__S5_4 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__sb__db__em__ep__db__sb__S5_4(Basic_Sfuncs* _BS);
  ~V2_4__sb__db__em__ep__db__sb__S5_4();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M12();
  void Calculate_M18();
  void Calculate_M30();
  void Calculate_M33();
  void Calculate_M45();
  void Calculate_M51();
  void Calculate_M63();
};
}

#endif
