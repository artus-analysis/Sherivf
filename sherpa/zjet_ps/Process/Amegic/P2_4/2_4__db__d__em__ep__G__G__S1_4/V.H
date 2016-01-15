//Header file for process V2_4__db__d__em__ep__G__G__S1_4

#ifndef V2_4__db__d__em__ep__G__G__S1_4_on
#define V2_4__db__d__em__ep__G__G__S1_4_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__db__d__em__ep__G__G__S1_4(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__db__d__em__ep__G__G__S1_4 : public Values,
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
  V2_4__db__d__em__ep__G__G__S1_4(Basic_Sfuncs* _BS);
  ~V2_4__db__d__em__ep__G__G__S1_4();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_1();
  void Calculate_2();
  void Calculate_3();
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
  void Calculate_M18();
  void Calculate_M19();
  void Calculate_M28();
  void Calculate_M29();
  void Calculate_M30();
  void Calculate_M31();
  void Calculate_M32();
  void Calculate_M33();
  void Calculate_M34();
  void Calculate_M35();
  void Calculate_M44();
  void Calculate_M45();
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
