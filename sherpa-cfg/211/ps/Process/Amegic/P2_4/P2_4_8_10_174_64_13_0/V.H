//Header file for process VP2_4_8_10_174_64_13_0

#ifndef VP2_4_8_10_174_64_13_0_on
#define VP2_4_8_10_174_64_13_0_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_VP2_4_8_10_174_64_13_0(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class VP2_4_8_10_174_64_13_0 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  VP2_4_8_10_174_64_13_0(Basic_Sfuncs* _BS);
  ~VP2_4_8_10_174_64_13_0();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 10; }
  Complex Evaluate(int,int);
  void    Calculate();
  void Calculate_M0();
  void Calculate_M3();
  void Calculate_M12();
  void Calculate_M15();
  void Calculate_M48();
  void Calculate_M51();
  void Calculate_M60();
  void Calculate_M63();
};
}

#endif
