#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__u__em__ep__G__G__S0_1(Basic_Sfuncs* bs) {
  return new V2_4__ub__u__em__ep__G__G__S0_1(bs);
}

V2_4__ub__u__em__ep__G__G__S0_1::V2_4__ub__u__em__ep__G__G__S0_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[570];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__ub__u__em__ep__G__G__S0_1::~V2_4__ub__u__em__ep__G__G__S0_1()
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

Complex V2_4__ub__u__em__ep__G__G__S0_1::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 2: Calculate_M2(); break;
    case 3: Calculate_M3(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 14: Calculate_M14(); break;
    case 15: Calculate_M15(); break;
    case 16: Calculate_M16(); break;
    case 17: Calculate_M17(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 28: Calculate_M28(); break;
    case 29: Calculate_M29(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
    case 32: Calculate_M32(); break;
    case 33: Calculate_M33(); break;
    case 34: Calculate_M34(); break;
    case 35: Calculate_M35(); break;
    case 44: Calculate_M44(); break;
    case 45: Calculate_M45(); break;
    case 46: Calculate_M46(); break;
    case 47: Calculate_M47(); break;
    case 48: Calculate_M48(); break;
    case 49: Calculate_M49(); break;
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 60: Calculate_M60(); break;
    case 61: Calculate_M61(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M0()
{
  M[0][0] = -(Z[32]*Z[27]-Z[18]*Z[7])*Z[51];
  M[0][1] = -(Z[84]*Z[80]+Z[72]*Z[68]-Z[60]*Z[55])*Z[90];
  M[0][2] = Z[108]*Z[92]*Z[91];
  M[0][3] = -(Z[71]*Z[135]-Z[59]*Z[117])*Z[146];
  M[0][4] = (Z[71]*Z[152]-Z[59]*Z[147])*Z[154];
  M[0][5] = Z[171]*Z[156]*Z[155];
  M[0][6] = -(Z[82]*Z[189]-Z[58]*Z[176])*Z[199];
  M[0][7] = (Z[82]*Z[204]-Z[58]*Z[200])*Z[206];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M1()
{
  M[1][0] = -(Z[215]*Z[27]-Z[209]*Z[7])*Z[51];
  M[1][1] = -(Z[84]*Z[185]+Z[72]*Z[130]-Z[60]*Z[112])*Z[90];
  M[1][2] = Z[108]*Z[92]*Z[99];
  M[1][3] = -(Z[71]*Z[228]-Z[59]*Z[226])*Z[146];
  M[1][4] = (Z[71]*Z[232]-Z[59]*Z[230])*Z[154];
  M[1][5] = Z[171]*Z[156]*Z[163];
  M[1][6] = -(Z[82]*Z[237]-Z[58]*Z[235])*Z[199];
  M[1][7] = (Z[82]*Z[241]-Z[58]*Z[239])*Z[206];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M2()
{
  M[2][0] = -(Z[48]*Z[250]-Z[23]*Z[245])*Z[51];
  M[2][1] = -(Z[254]*Z[88]+Z[252]*Z[76]-Z[60]*Z[64])*Z[90];
  M[2][2] = -(Z[106]*Z[257]-Z[92]*Z[255])*Z[108];
  M[2][3] = Z[146]*Z[59]*Z[126];
  M[2][4] = -Z[154]*Z[59]*Z[149];
  M[2][5] = -(Z[169]*Z[260]-Z[156]*Z[258])*Z[171];
  M[2][6] = Z[199]*Z[58]*Z[181];
  M[2][7] = -Z[206]*Z[58]*Z[201];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M3()
{
  M[3][0] = -(Z[224]*Z[250]-Z[212]*Z[245])*Z[51];
  M[3][1] = -(Z[254]*Z[193]+Z[252]*Z[139]-Z[60]*Z[121])*Z[90];
  M[3][2] = -(Z[225]*Z[257]-Z[92]*Z[256])*Z[108];
  M[3][3] = Z[146]*Z[59]*Z[227];
  M[3][4] = -Z[154]*Z[59]*Z[231];
  M[3][5] = -(Z[234]*Z[260]-Z[156]*Z[259])*Z[171];
  M[3][6] = Z[199]*Z[58]*Z[236];
  M[3][7] = -Z[206]*Z[58]*Z[240];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M12()
{
  M[12][0] = -(Z[43]*Z[266]-Z[18]*Z[263])*Z[51];
  M[12][1] = -(Z[84]*Z[281]+Z[72]*Z[275]-Z[60]*Z[269])*Z[90];
  M[12][2] = Z[108]*Z[92]*Z[285];
  M[12][3] = -(Z[71]*Z[308]-Z[59]*Z[294])*Z[146];
  M[12][4] = (Z[71]*Z[318]-Z[59]*Z[316])*Z[154];
  M[12][5] = Z[171]*Z[156]*Z[320];
  M[12][6] = -(Z[82]*Z[336]-Z[58]*Z[326])*Z[199];
  M[12][7] = (Z[82]*Z[345]-Z[58]*Z[343])*Z[206];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M13()
{
  M[13][0] = -(Z[221]*Z[266]-Z[209]*Z[263])*Z[51];
  M[13][1] = -(Z[84]*Z[333]+Z[72]*Z[304]-Z[60]*Z[290])*Z[90];
  M[13][2] = Z[108]*Z[92]*Z[286];
  M[13][3] = -(Z[71]*Z[349]-Z[59]*Z[347])*Z[146];
  M[13][4] = (Z[71]*Z[353]-Z[59]*Z[351])*Z[154];
  M[13][5] = Z[171]*Z[156]*Z[321];
  M[13][6] = -(Z[82]*Z[357]-Z[58]*Z[355])*Z[199];
  M[13][7] = (Z[82]*Z[361]-Z[58]*Z[359])*Z[206];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M14()
{
  M[14][0] = -(Z[37]*Z[367]-Z[23]*Z[364])*Z[51];
  M[14][1] = -(Z[254]*Z[284]+Z[252]*Z[278]-Z[60]*Z[272])*Z[90];
  M[14][2] = -(Z[106]*Z[370]-Z[92]*Z[368])*Z[108];
  M[14][3] = Z[146]*Z[59]*Z[301];
  M[14][4] = -Z[154]*Z[59]*Z[317];
  M[14][5] = -(Z[169]*Z[373]-Z[156]*Z[371])*Z[171];
  M[14][6] = Z[199]*Z[58]*Z[330];
  M[14][7] = -Z[206]*Z[58]*Z[344];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M15()
{
  M[15][0] = -(Z[218]*Z[367]-Z[212]*Z[364])*Z[51];
  M[15][1] = -(Z[254]*Z[339]+Z[252]*Z[311]-Z[60]*Z[297])*Z[90];
  M[15][2] = -(Z[225]*Z[370]-Z[92]*Z[369])*Z[108];
  M[15][3] = Z[146]*Z[59]*Z[348];
  M[15][4] = -Z[154]*Z[59]*Z[352];
  M[15][5] = -(Z[234]*Z[373]-Z[156]*Z[372])*Z[171];
  M[15][6] = Z[199]*Z[58]*Z[356];
  M[15][7] = -Z[206]*Z[58]*Z[360];
}

void V2_4__ub__u__em__ep__G__G__S0_1::Calculate_M16()
{
  M[16][0] = -(Z[382]*Z[27]-Z[378]*Z[7])*Z[51];
  M[16][1] = -(Z[393]*Z[80]+Z[391]*Z[68]-Z[390]*Z[55])*Z[90];
  M[16][2] = Z[108]*Z[92]*Z[394];
  M[16][3] = Z[146]*Z[389]*Z[117];
  M[16][4] = -Z[154]*Z[389]*Z[147];
  M[16][5] = -(Z[409]*Z[166]-Z[408]*Z[155])*Z[171];
  M[16][6] = -(Z[82]*Z[412]-Z[58]*Z[410])*Z[199];
  M[16][7] = (Z[82]*Z[418]-Z[58]*Z[414])*Z[206];
}

