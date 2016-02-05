#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__ub__em__ep__ub__ub__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__ub__ub__em__ep__ub__ub__S4_1(bs);
}

V2_4__ub__ub__em__ep__ub__ub__S4_1::V2_4__ub__ub__em__ep__ub__ub__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[7];
  Z = new Complex[310];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__ub__ub__em__ep__ub__ub__S4_1::~V2_4__ub__ub__em__ep__ub__ub__S4_1()
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

Complex V2_4__ub__ub__em__ep__ub__ub__S4_1::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
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
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M0()
{
  M[0][0] = (Z[8]*Z[1]+Z[14]*Z[10])*Z[21];
  M[0][1] = (Z[26]*Z[22]+Z[35]*Z[31])*Z[49];
  M[0][2] = -(Z[56]*Z[52]-Z[60]*Z[1])*Z[63];
  M[0][3] = (Z[67]*Z[1]+Z[72]*Z[68])*Z[76];
  M[0][4] = -(Z[67]*Z[77]+Z[72]*Z[79])*Z[84];
  M[0][5] = -(Z[35]*Z[85]+Z[26]*Z[86])*Z[87];
  M[0][6] = (Z[56]*Z[89]-Z[60]*Z[77])*Z[91];
  M[0][7] = -(Z[8]*Z[77]+Z[14]*Z[92])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M1()
{
  M[1][0] = (Z[8]*Z[95]+Z[14]*Z[97])*Z[21];
  M[1][1] = (Z[104]*Z[22]+Z[112]*Z[31])*Z[49];
  M[1][2] = -(Z[56]*Z[126]-Z[60]*Z[95])*Z[63];
  M[1][3] = (Z[67]*Z[95]+Z[72]*Z[127])*Z[76];
  M[1][4] = -(Z[67]*Z[129]+Z[72]*Z[131])*Z[84];
  M[1][5] = -(Z[112]*Z[85]+Z[104]*Z[86])*Z[87];
  M[1][6] = (Z[56]*Z[136]-Z[60]*Z[129])*Z[91];
  M[1][7] = -(Z[8]*Z[129]+Z[14]*Z[137])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M12()
{
  M[12][0] = (Z[161]*Z[1]+Z[164]*Z[16])*Z[21];
  M[12][1] = (Z[167]*Z[22]+Z[173]*Z[31])*Z[49];
  M[12][2] = -(Z[185]*Z[50]-Z[188]*Z[1])*Z[63];
  M[12][3] = (Z[191]*Z[1]+Z[194]*Z[73])*Z[76];
  M[12][4] = -(Z[191]*Z[77]+Z[194]*Z[81])*Z[84];
  M[12][5] = -(Z[173]*Z[85]+Z[167]*Z[86])*Z[87];
  M[12][6] = (Z[185]*Z[88]-Z[188]*Z[77])*Z[91];
  M[12][7] = -(Z[161]*Z[77]+Z[164]*Z[93])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M13()
{
  M[13][0] = (Z[161]*Z[95]+Z[164]*Z[99])*Z[21];
  M[13][1] = (Z[197]*Z[22]+Z[203]*Z[31])*Z[49];
  M[13][2] = -(Z[185]*Z[125]-Z[188]*Z[95])*Z[63];
  M[13][3] = (Z[191]*Z[95]+Z[194]*Z[128])*Z[76];
  M[13][4] = -(Z[191]*Z[129]+Z[194]*Z[133])*Z[84];
  M[13][5] = -(Z[203]*Z[85]+Z[197]*Z[86])*Z[87];
  M[13][6] = (Z[185]*Z[135]-Z[188]*Z[129])*Z[91];
  M[13][7] = -(Z[161]*Z[129]+Z[164]*Z[138])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M16()
{
  M[16][0] = (Z[220]*Z[9]+Z[225]*Z[18])*Z[21];
  M[16][1] = (Z[30]*Z[22]-Z[47]*Z[226])*Z[49];
  M[16][2] = -(Z[56]*Z[228]-Z[60]*Z[9])*Z[63];
  M[16][3] = (Z[67]*Z[9]+Z[72]*Z[229])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M17()
{
  M[17][0] = (Z[220]*Z[96]+Z[225]*Z[100])*Z[21];
  M[17][1] = (Z[108]*Z[22]-Z[124]*Z[226])*Z[49];
  M[17][2] = -(Z[56]*Z[234]-Z[60]*Z[96])*Z[63];
  M[17][3] = (Z[67]*Z[96]+Z[72]*Z[235])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M18()
{
  M[18][4] = -(Z[67]*Z[150]+Z[72]*Z[243])*Z[84];
  M[18][5] = -(Z[35]*Z[247]-Z[43]*Z[226])*Z[87];
  M[18][6] = (Z[142]*Z[231]-Z[146]*Z[150])*Z[91];
  M[18][7] = -(Z[220]*Z[150]+Z[225]*Z[152])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M19()
{
  M[19][4] = -(Z[67]*Z[156]+Z[72]*Z[252])*Z[84];
  M[19][5] = -(Z[112]*Z[247]-Z[120]*Z[226])*Z[87];
  M[19][6] = (Z[142]*Z[237]-Z[146]*Z[156])*Z[91];
  M[19][7] = -(Z[220]*Z[156]+Z[225]*Z[158])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M28()
{
  M[28][0] = (Z[257]*Z[9]+Z[260]*Z[15])*Z[21];
  M[28][1] = (Z[170]*Z[22]-Z[182]*Z[226])*Z[49];
  M[28][2] = -(Z[185]*Z[227]-Z[188]*Z[9])*Z[63];
  M[28][3] = (Z[191]*Z[9]+Z[194]*Z[230])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M29()
{
  M[29][0] = (Z[257]*Z[96]+Z[260]*Z[98])*Z[21];
  M[29][1] = (Z[200]*Z[22]-Z[212]*Z[226])*Z[49];
  M[29][2] = -(Z[185]*Z[233]-Z[188]*Z[96])*Z[63];
  M[29][3] = (Z[191]*Z[96]+Z[194]*Z[236])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M30()
{
  M[30][4] = -(Z[191]*Z[150]+Z[194]*Z[245])*Z[84];
  M[30][5] = -(Z[173]*Z[247]-Z[179]*Z[226])*Z[87];
  M[30][6] = (Z[215]*Z[232]-Z[217]*Z[150])*Z[91];
  M[30][7] = -(Z[257]*Z[150]+Z[260]*Z[151])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M31()
{
  M[31][4] = -(Z[191]*Z[156]+Z[194]*Z[254])*Z[84];
  M[31][5] = -(Z[203]*Z[247]-Z[209]*Z[226])*Z[87];
  M[31][6] = (Z[215]*Z[238]-Z[217]*Z[156])*Z[91];
  M[31][7] = -(Z[257]*Z[156]+Z[260]*Z[157])*Z[94];
}

void V2_4__ub__ub__em__ep__ub__ub__S4_1::Calculate_M32()
{
  M[32][4] = -(Z[265]*Z[78]+Z[270]*Z[82])*Z[84];
  M[32][5] = -(Z[39]*Z[85]-Z[47]*Z[271])*Z[87];
  M[32][6] = (Z[56]*Z[273]-Z[60]*Z[78])*Z[91];
  M[32][7] = -(Z[8]*Z[78]+Z[14]*Z[274])*Z[94];
}

