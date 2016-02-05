//Header file for process V2_2__db__d__em__ep

#ifndef V2_2__db__d__em__ep_on
#define V2_2__db__d__em__ep_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_2__db__d__em__ep(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_2__db__d__em__ep : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_2__db__d__em__ep(Basic_Sfuncs* _BS);
  ~V2_2__db__d__em__ep();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 6; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M1();
  void Calculate_M2();
  void Calculate_M3();
  void Calculate_M12();
  void Calculate_M13();
  void Calculate_M14();
  void Calculate_M15();
};
}

#endif
