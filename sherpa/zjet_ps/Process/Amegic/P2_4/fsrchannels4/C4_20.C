#include "PHASIC++/Channels/Single_Channel.H"
#include "ATOOLS/Org/Run_Parameter.H"
#include "PHASIC++/Channels/Channel_Elements.H"
#include "PHASIC++/Channels/Vegas.H"

using namespace PHASIC;
using namespace ATOOLS;

namespace PHASIC {
  class C4_20 : public Single_Channel {
    Info_Key m_kI_2_3,m_kI_4_23,m_kI_5_234,m_kZS_205;
    Vegas* p_vegas;
  public:
    C4_20(int,int,Flavour*,Integration_Info * const);
    ~C4_20();
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

extern "C" Single_Channel * Getter_C4_20(int nin,int nout,Flavour* fl,Integration_Info * const info) {
  return new C4_20(nin,nout,fl,info);
}

void C4_20::GeneratePoint(Vec4D * p,Cut_Data * cuts,double * _ran)
{
  double *ran = p_vegas->GeneratePoint(_ran);
  for(int i=0;i<rannum;i++) rans[i]=ran[i];
  Vec4D p2345=p[0]+p[1];
  double s2345_max = p2345.Abs2();
  double s234_max = sqr(sqrt(s2345_max)-sqrt(ms[5]));
  double s4 = ms[4];
  double s45_min = cuts->Getscut(std::string("45"));
  double s23_max = sqr(sqrt(s2345_max)-sqrt(s45_min));
  double s2 = ms[2];
  double s3 = ms[3];
  double s23_min = cuts->Getscut(std::string("23"));
  Flavour fl23 = Flavour((kf_code)(23));
  Vec4D  p23;
  double s23 = CE.MassivePropMomenta(fl23.Mass(),fl23.Width(),1,s23_min,s23_max,ran[0]);
  double s234_min = cuts->Getscut(std::string("234"));
  s234_min = Max(s234_min,sqr(sqrt(s23)+sqrt(s4)));
  Vec4D  p234;
  double s234 = CE.ThresholdMomenta(1.5,2.*sqrt(s234_min),s234_min,s234_max,ran[1]);
  double s5 = ms[5];
  CE.Isotropic2Momenta(p2345,s5,s234,p[5],p234,ran[2],ran[3]);
  CE.Isotropic2Momenta(p234,s4,s23,p[4],p23,ran[4],ran[5]);
  CE.Isotropic2Momenta(p23,s2,s3,p[2],p[3],ran[6],ran[7]);
}

void C4_20::GenerateWeight(Vec4D* p,Cut_Data * cuts)
{
  double wt = 1.;
  Vec4D p2345=p[0]+p[1];
  double s2345_max = p2345.Abs2();
  double s234_max = sqr(sqrt(s2345_max)-sqrt(ms[5]));
  double s4 = ms[4];
  double s45_min = cuts->Getscut(std::string("45"));
  double s23_max = sqr(sqrt(s2345_max)-sqrt(s45_min));
  double s2 = ms[2];
  double s3 = ms[3];
  double s23_min = cuts->Getscut(std::string("23"));
  Flavour fl23 = Flavour((kf_code)(23));
  Vec4D  p23 = p[2]+p[3];
  double s23 = dabs(p23.Abs2());
  wt *= CE.MassivePropWeight(fl23.Mass(),fl23.Width(),1,s23_min,s23_max,s23,rans[0]);
  double s234_min = cuts->Getscut(std::string("234"));
  s234_min = Max(s234_min,sqr(sqrt(s23)+sqrt(s4)));
  Vec4D  p234 = p[2]+p[3]+p[4];
  double s234 = dabs(p234.Abs2());
  wt *= CE.ThresholdWeight(1.5,2.*sqrt(s234_min),s234_min,s234_max,s234,rans[1]);
  double s5 = ms[5];
  if (m_kI_5_234.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kI_5_234<<CE.Isotropic2Weight(p[5],p234,m_kI_5_234[0],m_kI_5_234[1]);
  wt *= m_kI_5_234.Weight();

  rans[2]= m_kI_5_234[0];
  rans[3]= m_kI_5_234[1];
  if (m_kI_4_23.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kI_4_23<<CE.Isotropic2Weight(p[4],p23,m_kI_4_23[0],m_kI_4_23[1]);
  wt *= m_kI_4_23.Weight();

  rans[4]= m_kI_4_23[0];
  rans[5]= m_kI_4_23[1];
  if (m_kI_2_3.Weight()==ATOOLS::UNDEFINED_WEIGHT)
    m_kI_2_3<<CE.Isotropic2Weight(p[2],p[3],m_kI_2_3[0],m_kI_2_3[1]);
  wt *= m_kI_2_3.Weight();

  rans[6]= m_kI_2_3[0];
  rans[7]= m_kI_2_3[1];
  double vw = p_vegas->GenerateWeight(rans);
  if (wt!=0.) wt = vw/wt/pow(2.*M_PI,4*3.-4.);

  weight = wt;
}

C4_20::C4_20(int nin,int nout,Flavour* fl,Integration_Info * const info)
       : Single_Channel(nin,nout,fl)
{
  name = std::string("C4_20");
  rannum = 8;
  rans  = new double[rannum];
  m_kI_2_3.Assign(std::string("I_2_3"),2,0,info);
  m_kI_4_23.Assign(std::string("I_4_23"),2,0,info);
  m_kI_5_234.Assign(std::string("I_5_234"),2,0,info);
  m_kZS_205.Assign(std::string("ZS_205"),2,0,info);
  p_vegas = new Vegas(rannum,100,name);
}

C4_20::~C4_20()
{
  delete p_vegas;
}

void C4_20::ISRInfo(int & type,double & mass,double & width)
{
  type  = 2;
  mass  = 205.1721;
  width = 0.;
}

void C4_20::AddPoint(double Value)
{
  Single_Channel::AddPoint(Value);
  p_vegas->AddPoint(Value,rans);
}
std::string C4_20::ChID()
{
  return std::string("CG2$I_2_3$I_4_23$I_5_234$MP23_23$MTH_234$ZS_205$");
}
