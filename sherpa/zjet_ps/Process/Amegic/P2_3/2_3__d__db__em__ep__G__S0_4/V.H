//Header file for process V2_3__d__db__em__ep__G__S0_4

#ifndef V2_3__d__db__em__ep__G__S0_4_on
#define V2_3__d__db__em__ep__G__S0_4_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_3__d__db__em__ep__G__S0_4(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_3__d__db__em__ep__G__S0_4 : public Values,
  public Basic_Zfunc,
  public Basic_Xfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_3__d__db__em__ep__G__S0_4(Basic_Sfuncs* _BS);
  ~V2_3__d__db__em__ep__G__S0_4();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 8; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M3();
  void Calculate_M12();
  void Calculate_M15();
  void Calculate_M16();
  void Calculate_M19();
  void Calculate_M28();
  void Calculate_M31();
};
}

#endif
