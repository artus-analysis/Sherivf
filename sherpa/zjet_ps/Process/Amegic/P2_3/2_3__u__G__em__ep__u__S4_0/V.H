//Header file for process V2_3__u__G__em__ep__u__S4_0

#ifndef V2_3__u__G__em__ep__u__S4_0_on
#define V2_3__u__G__em__ep__u__S4_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_3__u__G__em__ep__u__S4_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_3__u__G__em__ep__u__S4_0 : public Values,
  public Basic_Zfunc,
  public Basic_Xfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_3__u__G__em__ep__u__S4_0(Basic_Sfuncs* _BS);
  ~V2_3__u__G__em__ep__u__S4_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 8; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M2();
  void Calculate_M12();
  void Calculate_M14();
  void Calculate_M17();
  void Calculate_M19();
  void Calculate_M29();
  void Calculate_M31();
};
}

#endif
