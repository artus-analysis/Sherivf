#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__G__em__ep__G__ub__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__ub__G__em__ep__G__ub__S4_1(bs);
}

V2_4__ub__G__em__ep__G__ub__S4_1::V2_4__ub__G__em__ep__G__ub__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[568];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__ub__G__em__ep__G__ub__S4_1::~V2_4__ub__G__em__ep__G__ub__S4_1()
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

Complex V2_4__ub__G__em__ep__G__ub__S4_1::Evaluate(int m,int n)
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

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M0()
{
  M[0][0] = -(Z[20]*Z[19]-Z[47]*Z[46])*Z[63];
  M[0][1] = (Z[20]*Z[75]-Z[47]*Z[81])*Z[85];
  M[0][2] = -Z[113]*Z[13]*Z[108];
  M[0][3] = -(Z[122]*Z[8]+Z[126]*Z[70]-Z[124]*Z[37])*Z[128];
  M[0][4] = -(Z[132]*Z[89]+Z[140]*Z[94])*Z[153];
  M[0][5] = Z[170]*Z[155]*Z[154];
  M[0][6] = (Z[64]*Z[171]+Z[66]*Z[175])*Z[178];
  M[0][7] = -(Z[64]*Z[183]+Z[66]*Z[196])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M1()
{
  M[1][0] = -(Z[20]*Z[208]-Z[47]*Z[210])*Z[63];
  M[1][1] = (Z[20]*Z[212]-Z[47]*Z[214])*Z[85];
  M[1][2] = -(Z[206]*Z[108]-Z[1]*Z[104])*Z[113];
  M[1][3] = -(Z[122]*Z[12]+Z[126]*Z[192]-Z[124]*Z[41])*Z[128];
  M[1][4] = -(Z[218]*Z[89]+Z[224]*Z[94])*Z[153];
  M[1][5] = Z[170]*Z[155]*Z[162];
  M[1][6] = (Z[64]*Z[235]+Z[66]*Z[237])*Z[178];
  M[1][7] = -(Z[64]*Z[239]+Z[66]*Z[241])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M2()
{
  M[2][0] = -Z[63]*Z[243]*Z[19];
  M[2][1] = Z[85]*Z[243]*Z[75];
  M[2][2] = -(Z[13]*Z[258]-Z[1]*Z[250])*Z[113];
  M[2][3] = -(Z[265]*Z[8]+Z[267]*Z[70]-Z[266]*Z[37])*Z[128];
  M[2][4] = -(Z[268]*Z[89]+Z[270]*Z[94])*Z[153];
  M[2][5] = Z[170]*Z[275]*Z[165];
  M[2][6] = (Z[64]*Z[276]+Z[66]*Z[280])*Z[178];
  M[2][7] = -(Z[64]*Z[283]+Z[66]*Z[285])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M3()
{
  M[3][0] = -Z[63]*Z[243]*Z[208];
  M[3][1] = Z[85]*Z[243]*Z[212];
  M[3][2] = -(Z[206]*Z[258]-Z[1]*Z[254])*Z[113];
  M[3][3] = -(Z[265]*Z[12]+Z[267]*Z[192]-Z[266]*Z[41])*Z[128];
  M[3][4] = -(Z[287]*Z[89]+Z[289]*Z[94])*Z[153];
  M[3][5] = Z[170]*Z[293]*Z[165];
  M[3][6] = (Z[64]*Z[294]+Z[66]*Z[296])*Z[178];
  M[3][7] = -(Z[64]*Z[298]+Z[66]*Z[300])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M12()
{
  M[12][0] = -(Z[20]*Z[311]-Z[47]*Z[331])*Z[63];
  M[12][1] = (Z[20]*Z[348]-Z[47]*Z[350])*Z[85];
  M[12][2] = -Z[113]*Z[13]*Z[359];
  M[12][3] = -(Z[122]*Z[304]+Z[126]*Z[344]-Z[124]*Z[324])*Z[128];
  M[12][4] = -(Z[132]*Z[354]+Z[148]*Z[357])*Z[153];
  M[12][5] = Z[170]*Z[155]*Z[360];
  M[12][6] = (Z[64]*Z[363]+Z[66]*Z[365])*Z[178];
  M[12][7] = -(Z[64]*Z[370]+Z[66]*Z[380])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M13()
{
  M[13][0] = -(Z[20]*Z[387]-Z[47]*Z[389])*Z[63];
  M[13][1] = (Z[20]*Z[391]-Z[47]*Z[393])*Z[85];
  M[13][2] = -(Z[206]*Z[359]-Z[1]*Z[358])*Z[113];
  M[13][3] = -(Z[122]*Z[307]+Z[126]*Z[377]-Z[124]*Z[327])*Z[128];
  M[13][4] = -(Z[218]*Z[354]+Z[230]*Z[357])*Z[153];
  M[13][5] = Z[170]*Z[155]*Z[361];
  M[13][6] = (Z[64]*Z[395]+Z[66]*Z[397])*Z[178];
  M[13][7] = -(Z[64]*Z[399]+Z[66]*Z[401])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M14()
{
  M[14][0] = -Z[63]*Z[243]*Z[311];
  M[14][1] = Z[85]*Z[243]*Z[348];
  M[14][2] = -(Z[13]*Z[405]-Z[1]*Z[403])*Z[113];
  M[14][3] = -(Z[265]*Z[304]+Z[267]*Z[344]-Z[266]*Z[324])*Z[128];
  M[14][4] = -(Z[268]*Z[354]+Z[272]*Z[357])*Z[153];
  M[14][5] = Z[170]*Z[275]*Z[362];
  M[14][6] = (Z[64]*Z[406]+Z[66]*Z[408])*Z[178];
  M[14][7] = -(Z[64]*Z[410]+Z[66]*Z[412])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M15()
{
  M[15][0] = -Z[63]*Z[243]*Z[387];
  M[15][1] = Z[85]*Z[243]*Z[391];
  M[15][2] = -(Z[206]*Z[405]-Z[1]*Z[404])*Z[113];
  M[15][3] = -(Z[265]*Z[307]+Z[267]*Z[377]-Z[266]*Z[327])*Z[128];
  M[15][4] = -(Z[287]*Z[354]+Z[291]*Z[357])*Z[153];
  M[15][5] = Z[170]*Z[293]*Z[362];
  M[15][6] = (Z[64]*Z[414]+Z[66]*Z[416])*Z[178];
  M[15][7] = -(Z[64]*Z[418]+Z[66]*Z[420])*Z[205];
}

void V2_4__ub__G__em__ep__G__ub__S4_1::Calculate_M16()
{
  M[16][0] = -(Z[20]*Z[425]-Z[47]*Z[427])*Z[63];
  M[16][1] = (Z[20]*Z[432]-Z[47]*Z[438])*Z[85];
  M[16][2] = -Z[113]*Z[423]*Z[108];
  M[16][3] = -(Z[444]*Z[8]+Z[446]*Z[70]-Z[445]*Z[37])*Z[128];
  M[16][4] = -(Z[448]*Z[89]+Z[452]*Z[94])*Z[153];
  M[16][5] = Z[170]*Z[155]*Z[459];
  M[16][6] = (Z[429]*Z[171]+Z[431]*Z[175])*Z[178];
  M[16][7] = -(Z[429]*Z[183]+Z[431]*Z[196])*Z[205];
}

