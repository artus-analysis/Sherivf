//Header file for process V2_4__ub__u__em__ep__c__cb

#ifndef V2_4__ub__u__em__ep__c__cb_on
#define V2_4__ub__u__em__ep__c__cb_on
#include "AMEGIC++/String/Values.H"

extern "C" AMEGIC::Values* Getter_V2_4__ub__u__em__ep__c__cb(AMEGIC::Basic_Sfuncs* bs);

namespace AMEGIC {

class V2_4__ub__u__em__ep__c__cb : public Values,
  public Basic_Zfunc,
  public Basic_Pfunc {
  Complex*  Z;
  int*      f;
  Complex*  c;
  Complex** M;
  int*      cl;
public:
  V2_4__ub__u__em__ep__c__cb(Basic_Sfuncs* _BS);
  ~V2_4__ub__u__em__ep__c__cb();
  void SetCouplFlav(std::vector<Complex>&);
  int NumberOfCouplings() { return 7; }
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
