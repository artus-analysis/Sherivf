#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__u__em__ep__G__G__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__ub__u__em__ep__G__G__S4_1(bs);
}

V2_4__ub__u__em__ep__G__G__S4_1::V2_4__ub__u__em__ep__G__G__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[578];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__ub__u__em__ep__G__G__S4_1::~V2_4__ub__u__em__ep__G__G__S4_1()
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

Complex V2_4__ub__u__em__ep__G__G__S4_1::Evaluate(int m,int n)
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

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M0()
{
  M[0][0] = -(Z[32]*Z[27]-Z[18]*Z[7])*Z[51];
  M[0][1] = -(Z[84]*Z[80]+Z[72]*Z[68]-Z[60]*Z[55])*Z[90];
  M[0][2] = Z[108]*Z[92]*Z[91];
  M[0][3] = -(Z[71]*Z[135]-Z[59]*Z[117])*Z[146];
  M[0][4] = (Z[71]*Z[152]-Z[59]*Z[147])*Z[154];
  M[0][5] = -(Z[167]*Z[166]-Z[156]*Z[155])*Z[172];
  M[0][6] = -(Z[82]*Z[190]-Z[58]*Z[177])*Z[200];
  M[0][7] = (Z[82]*Z[206]-Z[58]*Z[201])*Z[209];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M1()
{
  M[1][0] = -(Z[218]*Z[27]-Z[212]*Z[7])*Z[51];
  M[1][1] = -(Z[84]*Z[186]+Z[72]*Z[130]-Z[60]*Z[112])*Z[90];
  M[1][2] = Z[108]*Z[92]*Z[99];
  M[1][3] = -(Z[71]*Z[231]-Z[59]*Z[229])*Z[146];
  M[1][4] = (Z[71]*Z[235]-Z[59]*Z[233])*Z[154];
  M[1][5] = -(Z[237]*Z[166]-Z[156]*Z[163])*Z[172];
  M[1][6] = -(Z[82]*Z[241]-Z[58]*Z[239])*Z[200];
  M[1][7] = (Z[82]*Z[245]-Z[58]*Z[243])*Z[209];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M2()
{
  M[2][0] = -(Z[48]*Z[254]-Z[23]*Z[249])*Z[51];
  M[2][1] = -(Z[258]*Z[88]+Z[256]*Z[76]-Z[60]*Z[64])*Z[90];
  M[2][2] = -(Z[106]*Z[261]-Z[92]*Z[259])*Z[108];
  M[2][3] = -(Z[202]*Z[144]-Z[59]*Z[126])*Z[146];
  M[2][4] = (Z[202]*Z[153]-Z[59]*Z[149])*Z[154];
  M[2][5] = -(Z[170]*Z[264]-Z[156]*Z[262])*Z[172];
  M[2][6] = Z[200]*Z[58]*Z[182];
  M[2][7] = -Z[209]*Z[58]*Z[203];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M3()
{
  M[3][0] = -(Z[227]*Z[254]-Z[215]*Z[249])*Z[51];
  M[3][1] = -(Z[258]*Z[194]+Z[256]*Z[139]-Z[60]*Z[121])*Z[90];
  M[3][2] = -(Z[228]*Z[261]-Z[92]*Z[260])*Z[108];
  M[3][3] = -(Z[202]*Z[232]-Z[59]*Z[230])*Z[146];
  M[3][4] = (Z[202]*Z[236]-Z[59]*Z[234])*Z[154];
  M[3][5] = -(Z[238]*Z[264]-Z[156]*Z[263])*Z[172];
  M[3][6] = Z[200]*Z[58]*Z[240];
  M[3][7] = -Z[209]*Z[58]*Z[244];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M12()
{
  M[12][0] = -(Z[43]*Z[270]-Z[18]*Z[267])*Z[51];
  M[12][1] = -(Z[84]*Z[285]+Z[72]*Z[279]-Z[60]*Z[273])*Z[90];
  M[12][2] = Z[108]*Z[92]*Z[289];
  M[12][3] = -(Z[71]*Z[312]-Z[59]*Z[298])*Z[146];
  M[12][4] = (Z[71]*Z[322]-Z[59]*Z[320])*Z[154];
  M[12][5] = -(Z[167]*Z[326]-Z[156]*Z[324])*Z[172];
  M[12][6] = -(Z[82]*Z[340]-Z[58]*Z[330])*Z[200];
  M[12][7] = (Z[82]*Z[349]-Z[58]*Z[347])*Z[209];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M13()
{
  M[13][0] = -(Z[224]*Z[270]-Z[212]*Z[267])*Z[51];
  M[13][1] = -(Z[84]*Z[337]+Z[72]*Z[308]-Z[60]*Z[294])*Z[90];
  M[13][2] = Z[108]*Z[92]*Z[290];
  M[13][3] = -(Z[71]*Z[353]-Z[59]*Z[351])*Z[146];
  M[13][4] = (Z[71]*Z[357]-Z[59]*Z[355])*Z[154];
  M[13][5] = -(Z[237]*Z[326]-Z[156]*Z[325])*Z[172];
  M[13][6] = -(Z[82]*Z[361]-Z[58]*Z[359])*Z[200];
  M[13][7] = (Z[82]*Z[365]-Z[58]*Z[363])*Z[209];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M14()
{
  M[14][0] = -(Z[37]*Z[371]-Z[23]*Z[368])*Z[51];
  M[14][1] = -(Z[258]*Z[288]+Z[256]*Z[282]-Z[60]*Z[276])*Z[90];
  M[14][2] = -(Z[106]*Z[374]-Z[92]*Z[372])*Z[108];
  M[14][3] = -(Z[202]*Z[319]-Z[59]*Z[305])*Z[146];
  M[14][4] = (Z[202]*Z[323]-Z[59]*Z[321])*Z[154];
  M[14][5] = -(Z[170]*Z[377]-Z[156]*Z[375])*Z[172];
  M[14][6] = Z[200]*Z[58]*Z[334];
  M[14][7] = -Z[209]*Z[58]*Z[348];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M15()
{
  M[15][0] = -(Z[221]*Z[371]-Z[215]*Z[368])*Z[51];
  M[15][1] = -(Z[258]*Z[343]+Z[256]*Z[315]-Z[60]*Z[301])*Z[90];
  M[15][2] = -(Z[228]*Z[374]-Z[92]*Z[373])*Z[108];
  M[15][3] = -(Z[202]*Z[354]-Z[59]*Z[352])*Z[146];
  M[15][4] = (Z[202]*Z[358]-Z[59]*Z[356])*Z[154];
  M[15][5] = -(Z[238]*Z[377]-Z[156]*Z[376])*Z[172];
  M[15][6] = Z[200]*Z[58]*Z[360];
  M[15][7] = -Z[209]*Z[58]*Z[364];
}

void V2_4__ub__u__em__ep__G__G__S4_1::Calculate_M16()
{
  M[16][0] = -(Z[386]*Z[27]-Z[382]*Z[7])*Z[51];
  M[16][1] = -(Z[398]*Z[80]+Z[396]*Z[68]-Z[394]*Z[55])*Z[90];
  M[16][2] = Z[108]*Z[92]*Z[399];
  M[16][3] = -(Z[395]*Z[135]-Z[393]*Z[117])*Z[146];
  M[16][4] = (Z[395]*Z[152]-Z[393]*Z[147])*Z[154];
  M[16][5] = -(Z[414]*Z[166]-Z[413]*Z[155])*Z[172];
  M[16][6] = -(Z[82]*Z[418]-Z[58]*Z[416])*Z[200];
  M[16][7] = (Z[82]*Z[425]-Z[58]*Z[420])*Z[209];
}

