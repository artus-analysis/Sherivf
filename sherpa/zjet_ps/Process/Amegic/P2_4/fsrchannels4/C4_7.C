#include "PHASIC++/Channels/Single_Channel.H"
#include "ATOOLS/Org/Run_Parameter.H"
#include "PHASIC++/Channels/Channel_Elements.H"
#include "PHASIC++/Channels/Vegas.H"

using namespace PHASIC;
using namespace ATOOLS;

namespace PHASIC {
  class C4_7 : public Single_Channel {
    double m_amct,m_alpha,m_ctmax,m_ctmin;
    Info_Key m_kI_2_3,m_kTC_0_4_1__5_23,m_kTC_0__1__4_235,m_kZS_205;
    Vegas* p_vegas;
  public:
    C4_7(int,int,Flavour*,Integration_Info * const);
    ~C4_7();
    void   GenerateWeight(Vec4D *,Cut_Data *);
    void   GeneratePoint(Vec4D *,Cut_Data *,double *);
    void   AddPoint(double);
    void   MPISync()                 { p_vegas->MPISync(); }
    void   Optimize()                { p_vegas->Optimize(); } 
    void   EndOptimize()             { p_vegas->EndOptimize(); } 
    void   WriteOut(std::string pId) { p_vegas->WriteOut(pId); } 
    void   ReadIn(std::string pId)   { p_vegas->ReadIn(pId); } 
    void   ISRInfo(int &,double &,double &);
    std::string ChID();
  };
}

extern "C" Single_Channel * Getter_C4_7(int nin,int nout,Flavour* fl,Integration_Info * const info) {
  return new C4_7(nin,nout,fl,info);
}

void C4_7::GeneratePoint(Vec4D * p,Cut_Data * cuts,double * _ran)
{
  double *ran = p_vegas->GeneratePoint(_ran);
  for(int i=0;i<rannum;i++) rans[i]=ran[i];
  Vec4D p2345=p[0]+p[1];
  double s2345_max = p2345.Abs2();
  double s235_max = sqr(sqrt(s2345_max)-sqrt(ms[4]));
  double s45_min = cuts->Getscut(std::string("45"));
  double s23_max = sqr(sqrt(s2345_max)-sqrt(s45_min));
  double s2 = ms[2];
  double s3 = ms[3];
  double s23_min = cuts->Getscut(std::string("23"));
  Flavour fl23 = Flavour((kf_code)(23));
  Vec4D  p23;
  double s23 = CE.MassivePropMomenta(fl23.Mass(),fl23.Width(),1,s23_min,s23_max,ran[0]);
  double s5 = ms[5];
  double s235_min = cuts->Getscut(std::string("235"));
  s235_min = Max(s235_min,sqr(sqrt(s5)+sqrt(s23)));
  Vec4D  p235;
  double s235 = CE.ThresholdMomenta(1.5,2.*sqrt(s235_min),s235_min,s235_max,ran[1]);
  double s4 = ms[4];
  m_ctmax = cuts->cosmax[0][4];
  m_ctmin = cuts->cosmin[0][4];
  CE.TChannelMomenta(p[0],p[1],p[4],p235,s4,s235,0.,m_alpha,m_ctmax,m_ctmin,m_amct,0,ran[2],ran[3]);
  Vec4D  p0_4 = p[0]-p[4];
  CE.TChannelMomenta(p0_4,p[1],p[5],p23,s5,s23,0.,m_alpha,1.,-1.,m_amct,0,ran[4],ran[5]);
  CE.Isotropic2Momenta(p23,s2,s3,p[2],p[3],ran[6],ran[7]);
}

void C4_7::GenerateWeight(Vec4D* p,Cut_Data * cuts)
{
  double wt = 1.;
  Vec4D p2345=p[0]+p[1];
  double s2345_max = p2345.Abs2();
  double s235_max = sqr(sqrt(s2345_max)-sqrt(ms[4]));
  double s45_min = cuts->Getscut(std::string("45"));
  double s23_max = sqr(sqrt(s2345_max)-sqrt(s45_min));
  double s2 = ms[2];
  double s3 = ms[3];
  double s23_min = cuts->Getscut(std::string("23"));
  Flavour fl23 = Flavour((kf_code)(23));
  Vec4D  p23 = p[2]+p[3];
  double s23 = dabs(p23.Abs2());
  wt *= CE.MassivePropWeight(fl23.Mass(),fl23.Width(),1,s23_min,s23_max,s23,rans[0]);
  double s5 = ms[5];
  double s235_min = cuts->Getscut(std::string("235"));
  s235_min = Max(s235_min,sqr(sqrt(s5)+sqrt(s23)));
  Vec4D  p235 = p[2]+p[3]+p[5];
  double s235 = dabs(p235.Abs2());
  wt *= CE.ThresholdWeight(1.5,2.*sqrt(s235_min),s235_min,s235_max,s235,rans[1]);
  double s4 = ms[4];
  m_ctmax = cuts->cosmax[0][4];
  m_ctmin = cuts->cosmin[0][4];
  if (m_kTC_0__1__4_235.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kTC_0__1__4_235<<CE.TChannelWeight(p[0],p[1],p[4],p235,0.,m_alpha,m_ctmax,m_ctmin,m_amct,0,m_kTC_0__1__4_235[0],m_kTC_0__1__4_235[1]);
  wt *= m_kTC_0__1__4_235.Weight();

  rans[2]= m_kTC_0__1__4_235[0];
  rans[3]= m_kTC_0__1__4_235[1];
  Vec4D  p0_4 = p[0]-p[4];
  if (m_kTC_0_4_1__5_23.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kTC_0_4_1__5_23<<CE.TChannelWeight(p0_4,p[1],p[5],p23,0.,m_alpha,1.,-1.,m_amct,0,m_kTC_0_4_1__5_23[0],m_kTC_0_4_1__5_23[1]);
  wt *= m_kTC_0_4_1__5_23.Weight();

  rans[4]= m_kTC_0_4_1__5_23[0];
  rans[5]= m_kTC_0_4_1__5_23[1];
  if (m_kI_2_3.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kI_2_3<<CE.Isotropic2Weight(p[2],p[3],m_kI_2_3[0],m_kI_2_3[1]);
  wt *= m_kI_2_3.Weight();

  rans[6]= m_kI_2_3[0];
  rans[7]= m_kI_2_3[1];
  double vw = p_vegas->GenerateWeight(rans);
  if (wt!=0.) wt = vw/wt/pow(2.*M_PI,4*3.-4.);

  weight = wt;
}

C4_7::C4_7(int nin,int nout,Flavour* fl,Integration_Info * const info)
       : Single_Channel(nin,nout,fl)
{
  name = std::string("C4_7");
  rannum = 8;
  rans  = new double[rannum];
  m_amct  = 1.;
  m_alpha = .9;
  m_ctmax = 1.;
  m_ctmin = -1.;
  m_kI_2_3.Assign(std::string("I_2_3"),2,0,info);
  m_kTC_0_4_1__5_23.Assign(std::string("TC_0_4_1__5_23"),2,0,info);
  m_kTC_0__1__4_235.Assign(std::string("TC_0__1__4_235"),2,0,info);
  m_kZS_205.Assign(std::string("ZS_205"),2,0,info);
  p_vegas = new Vegas(rannum,100,name);
}

C4_7::~C4_7()
{
  delete p_vegas;
}

void C4_7::ISRInfo(int & type,double & mass,double & width)
{
  type  = 2;
  mass  = 205.1721;
  width = 0.;
}

void C4_7::AddPoint(double Value)
{
  Single_Channel::AddPoint(Value);
  p_vegas->AddPoint(Value,rans);
}
std::string C4_7::ChID()
{
  return std::string("CG2$I_2_3$MP23_23$MTH_235$TC_0_4_1__5_23$TC_0__1__4_235$ZS_205$");
}
