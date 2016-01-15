#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__d__em__ep__G__d__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__G__d__em__ep__G__d__S4_1(bs);
}

V2_4__G__d__em__ep__G__d__S4_1::V2_4__G__d__em__ep__G__d__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[534];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__G__d__em__ep__G__d__S4_1::~V2_4__G__d__em__ep__G__d__S4_1()
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

Complex V2_4__G__d__em__ep__G__d__S4_1::Evaluate(int m,int n)
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

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M0()
{
  M[0][0] = (Z[19]*Z[18]+Z[46]*Z[45])*Z[62];
  M[0][1] = (Z[19]*Z[75]+Z[46]*Z[81])*Z[85];
  M[0][2] = -Z[117]*Z[1]*Z[101];
  M[0][3] = Z[136]*Z[132]*Z[131];
  M[0][4] = (Z[143]*Z[142]-Z[140]*Z[139])*Z[146];
  M[0][5] = (Z[143]*Z[176]-Z[140]*Z[155])*Z[189];
  M[0][6] = -(Z[201]*Z[92]+Z[204]*Z[98])*Z[206];
  M[0][7] = (Z[209]*Z[72]-Z[204]*Z[67])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M1()
{
  M[1][1] = (Z[19]*Z[216]+Z[46]*Z[222])*Z[85];
  M[1][3] = (Z[228]*Z[131]-Z[226]*Z[122])*Z[136];
  M[1][4] = Z[146]*Z[143]*Z[232];
  M[1][5] = (Z[143]*Z[236]-Z[140]*Z[234])*Z[189];
  M[1][6] = -(Z[242]*Z[92]+Z[243]*Z[98])*Z[206];
  M[1][7] = (Z[244]*Z[72]-Z[243]*Z[67])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M2()
{
  M[2][3] = -Z[136]*Z[128]*Z[257];
  M[2][5] = (Z[259]*Z[188]-Z[140]*Z[164])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M3()
{
  M[3][0] = (Z[19]*Z[271]+Z[46]*Z[273])*Z[62];
  M[3][2] = -(Z[270]*Z[108]+Z[269]*Z[101])*Z[117];
  M[3][3] = -(Z[227]*Z[257]+Z[226]*Z[256])*Z[136];
  M[3][5] = (Z[259]*Z[237]-Z[140]*Z[235])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M12()
{
  M[12][0] = (Z[19]*Z[289]+Z[46]*Z[309])*Z[62];
  M[12][1] = (Z[19]*Z[326]+Z[46]*Z[327])*Z[85];
  M[12][2] = -Z[117]*Z[1]*Z[334];
  M[12][3] = Z[136]*Z[132]*Z[339];
  M[12][4] = (Z[143]*Z[341]-Z[140]*Z[340])*Z[146];
  M[12][5] = (Z[143]*Z[364]-Z[140]*Z[348])*Z[189];
  M[12][6] = -(Z[198]*Z[330]+Z[204]*Z[333])*Z[206];
  M[12][7] = (Z[212]*Z[325]-Z[204]*Z[322])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M13()
{
  M[13][1] = (Z[19]*Z[374]+Z[46]*Z[375])*Z[85];
  M[13][3] = (Z[228]*Z[339]-Z[226]*Z[337])*Z[136];
  M[13][4] = Z[146]*Z[143]*Z[376];
  M[13][5] = (Z[143]*Z[379]-Z[140]*Z[377])*Z[189];
  M[13][6] = -(Z[241]*Z[330]+Z[243]*Z[333])*Z[206];
  M[13][7] = (Z[245]*Z[325]-Z[243]*Z[322])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M14()
{
  M[14][3] = -Z[136]*Z[128]*Z[389];
  M[14][5] = (Z[259]*Z[373]-Z[140]*Z[355])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M15()
{
  M[15][0] = (Z[19]*Z[391]+Z[46]*Z[393])*Z[62];
  M[15][2] = -(Z[270]*Z[335]+Z[269]*Z[334])*Z[117];
  M[15][3] = -(Z[227]*Z[389]+Z[226]*Z[388])*Z[136];
  M[15][5] = (Z[259]*Z[380]-Z[140]*Z[378])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M16()
{
  M[16][0] = (Z[397]*Z[18]+Z[398]*Z[45])*Z[62];
  M[16][1] = (Z[397]*Z[75]+Z[398]*Z[81])*Z[85];
  M[16][2] = -Z[117]*Z[1]*Z[405];
  M[16][3] = Z[136]*Z[132]*Z[432];
  M[16][4] = (Z[436]*Z[142]-Z[435]*Z[139])*Z[146];
  M[16][5] = (Z[436]*Z[176]-Z[435]*Z[155])*Z[189];
  M[16][6] = -(Z[441]*Z[92]+Z[442]*Z[98])*Z[206];
  M[16][7] = (Z[443]*Z[72]-Z[442]*Z[67])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M17()
{
  M[17][1] = (Z[397]*Z[216]+Z[398]*Z[222])*Z[85];
  M[17][3] = (Z[228]*Z[432]-Z[226]*Z[424])*Z[136];
  M[17][4] = Z[146]*Z[436]*Z[232];
  M[17][5] = (Z[436]*Z[236]-Z[435]*Z[234])*Z[189];
  M[17][6] = -(Z[447]*Z[92]+Z[448]*Z[98])*Z[206];
  M[17][7] = (Z[449]*Z[72]-Z[448]*Z[67])*Z[213];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M18()
{
  M[18][3] = -Z[136]*Z[128]*Z[452];
  M[18][5] = (Z[454]*Z[188]-Z[435]*Z[164])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M19()
{
  M[19][0] = (Z[397]*Z[271]+Z[398]*Z[273])*Z[62];
  M[19][2] = -(Z[270]*Z[412]+Z[269]*Z[405])*Z[117];
  M[19][3] = -(Z[227]*Z[452]+Z[226]*Z[451])*Z[136];
  M[19][5] = (Z[454]*Z[237]-Z[435]*Z[235])*Z[189];
}

void V2_4__G__d__em__ep__G__d__S4_1::Calculate_M28()
{
  M[28][0] = (Z[397]*Z[289]+Z[398]*Z[309])*Z[62];
  M[28][1] = (Z[397]*Z[326]+Z[398]*Z[327])*Z[85];
  M[28][2] = -Z[117]*Z[1]*Z[461];
  M[28][3] = Z[136]*Z[132]*Z[466];
  M[28][4] = (Z[436]*Z[341]-Z[435]*Z[340])*Z[146];
  M[28][5] = (Z[436]*Z[364]-Z[435]*Z[348])*Z[189];
  M[28][6] = -(Z[440]*Z[330]+Z[442]*Z[333])*Z[206];
  M[28][7] = (Z[444]*Z[325]-Z[442]*Z[322])*Z[213];
}

