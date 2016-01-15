//Header file for process V2_4__u__ub__em__ep__c__cb__S0_5

#ifndef V2_4__u__ub__em__ep__c__cb__S0_5_on
#define V2_4__u__ub__em__ep__c__cb__S0_5_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__u__ub__em__ep__c__cb__S0_5(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__u__ub__em__ep__c__cb__S0_5 : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__u__ub__em__ep__c__cb__S0_5(Basic_Sfuncs* _BS);
  ~V2_4__u__ub__em__ep__c__cb__S0_5();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
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
