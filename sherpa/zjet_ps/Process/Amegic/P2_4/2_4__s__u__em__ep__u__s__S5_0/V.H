//Header file for process V2_4__s__u__em__ep__u__s__S5_0

#ifndef V2_4__s__u__em__ep__u__s__S5_0_on
#define V2_4__s__u__em__ep__u__s__S5_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__s__u__em__ep__u__s__S5_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__s__u__em__ep__u__s__S5_0 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__s__u__em__ep__u__s__S5_0(Basic_Sfuncs* _BS);
  ~V2_4__s__u__em__ep__u__s__S5_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
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
