#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__u__em__ep__d__db__S0_5(Basic_Sfuncs* bs) {
  return new V2_4__ub__u__em__ep__d__db__S0_5(bs);
}

V2_4__ub__u__em__ep__d__db__S0_5::V2_4__ub__u__em__ep__d__db__S0_5(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[10];
  Z = new Complex[174];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__ub__u__em__ep__d__db__S0_5::~V2_4__ub__u__em__ep__d__db__S0_5()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<64;i++) delete[] M[i];
    delete[] M;
  }
}

Complex V2_4__ub__u__em__ep__d__db__S0_5::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 3: Calculate_M3(); break;
    case 12: Calculate_M12(); break;
    case 15: Calculate_M15(); break;
    case 48: Calculate_M48(); break;
    case 51: Calculate_M51(); break;
    case 60: Calculate_M60(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M0()
{
  M[0][0] = -(Z[13]*Z[9]-Z[8]*Z[1])*Z[18];
  M[0][1] = (Z[25]*Z[24]+Z[1]*Z[29])*Z[32];
  M[0][2] = -(Z[1]*Z[36]+Z[41]*Z[40])*Z[45];
  M[0][3] = -(Z[55]*Z[54]-Z[50]*Z[49])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M3()
{
  M[3][0] = -(Z[84]*Z[64]-Z[79]*Z[62])*Z[18];
  M[3][1] = (Z[87]*Z[24]+Z[62]*Z[29])*Z[32];
  M[3][2] = -(Z[62]*Z[36]+Z[88]*Z[40])*Z[45];
  M[3][3] = -(Z[85]*Z[76]-Z[50]*Z[68])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M12()
{
  M[12][0] = -(Z[95]*Z[14]-Z[92]*Z[1])*Z[18];
  M[12][1] = (Z[20]*Z[98]+Z[1]*Z[101])*Z[32];
  M[12][2] = -(Z[1]*Z[104]+Z[43]*Z[107])*Z[45];
  M[12][3] = -(Z[55]*Z[113]-Z[50]*Z[110])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M15()
{
  M[15][0] = -(Z[130]*Z[63]-Z[127]*Z[62])*Z[18];
  M[15][1] = (Z[86]*Z[98]+Z[62]*Z[101])*Z[32];
  M[15][2] = -(Z[62]*Z[104]+Z[89]*Z[107])*Z[45];
  M[15][3] = -(Z[85]*Z[125]-Z[50]*Z[119])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M48()
{
  M[48][0] = -(Z[13]*Z[167]-Z[8]*Z[139])*Z[18];
  M[48][1] = (Z[150]*Z[134]+Z[139]*Z[138])*Z[32];
  M[48][2] = -(Z[139]*Z[154]+Z[141]*Z[159])*Z[45];
  M[48][3] = -(Z[170]*Z[59]-Z[169]*Z[49])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M51()
{
  M[51][0] = -(Z[84]*Z[172]-Z[79]*Z[142])*Z[18];
  M[51][1] = (Z[160]*Z[134]+Z[142]*Z[138])*Z[32];
  M[51][2] = -(Z[142]*Z[154]+Z[144]*Z[159])*Z[45];
  M[51][3] = -(Z[173]*Z[72]-Z[169]*Z[68])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M60()
{
  M[60][0] = -(Z[95]*Z[168]-Z[92]*Z[139])*Z[18];
  M[60][1] = (Z[151]*Z[147]+Z[139]*Z[149])*Z[32];
  M[60][2] = -(Z[139]*Z[163]+Z[140]*Z[166])*Z[45];
  M[60][3] = -(Z[170]*Z[116]-Z[169]*Z[110])*Z[61];
}

void V2_4__ub__u__em__ep__d__db__S0_5::Calculate_M63()
{
  M[63][0] = -(Z[130]*Z[171]-Z[127]*Z[142])*Z[18];
  M[63][1] = (Z[161]*Z[147]+Z[142]*Z[149])*Z[32];
  M[63][2] = -(Z[142]*Z[163]+Z[143]*Z[166])*Z[45];
  M[63][3] = -(Z[173]*Z[122]-Z[169]*Z[119])*Z[61];
}

