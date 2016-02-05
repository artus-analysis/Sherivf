#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__d__d__em__ep__d__d__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__d__d__em__ep__d__d__S4_1(bs);
}

V2_4__d__d__em__ep__d__d__S4_1::V2_4__d__d__em__ep__d__d__S4_1(Basic_Sfuncs* _BS) :
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

V2_4__d__d__em__ep__d__d__S4_1::~V2_4__d__d__em__ep__d__d__S4_1()
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

Complex V2_4__d__d__em__ep__d__d__S4_1::Evaluate(int m,int n)
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

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M0()
{
  M[0][0] = (Z[10]*Z[9]+Z[15]*Z[14])*Z[18];
  M[0][1] = -(Z[27]*Z[26]-Z[15]*Z[22])*Z[31];
  M[0][2] = (Z[39]*Z[35]+Z[44]*Z[15])*Z[48];
  M[0][3] = (Z[61]*Z[60]+Z[70]*Z[69])*Z[76];
  M[0][4] = -(Z[78]*Z[39]+Z[79]*Z[44])*Z[81];
  M[0][5] = (Z[82]*Z[26]-Z[79]*Z[22])*Z[84];
  M[0][6] = -(Z[9]*Z[87]+Z[14]*Z[79])*Z[91];
  M[0][7] = -(Z[92]*Z[69]+Z[93]*Z[60])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M1()
{
  M[1][0] = (Z[96]*Z[9]+Z[97]*Z[14])*Z[18];
  M[1][1] = -(Z[98]*Z[26]-Z[97]*Z[22])*Z[31];
  M[1][2] = (Z[39]*Z[102]+Z[44]*Z[97])*Z[48];
  M[1][3] = (Z[61]*Z[116]+Z[70]*Z[124])*Z[76];
  M[1][4] = -(Z[130]*Z[39]+Z[131]*Z[44])*Z[81];
  M[1][5] = (Z[132]*Z[26]-Z[131]*Z[22])*Z[84];
  M[1][6] = -(Z[9]*Z[136]+Z[14]*Z[131])*Z[91];
  M[1][7] = -(Z[92]*Z[124]+Z[93]*Z[116])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M12()
{
  M[12][0] = (Z[5]*Z[161]+Z[15]*Z[164])*Z[18];
  M[12][1] = -(Z[29]*Z[170]-Z[15]*Z[167])*Z[31];
  M[12][2] = (Z[173]*Z[32]+Z[176]*Z[15])*Z[48];
  M[12][3] = (Z[61]*Z[185]+Z[70]*Z[191])*Z[76];
  M[12][4] = -(Z[77]*Z[173]+Z[79]*Z[176])*Z[81];
  M[12][5] = (Z[83]*Z[170]-Z[79]*Z[167])*Z[84];
  M[12][6] = -(Z[161]*Z[85]+Z[164]*Z[79])*Z[91];
  M[12][7] = -(Z[92]*Z[191]+Z[93]*Z[185])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M13()
{
  M[13][0] = (Z[95]*Z[161]+Z[97]*Z[164])*Z[18];
  M[13][1] = -(Z[99]*Z[170]-Z[97]*Z[167])*Z[31];
  M[13][2] = (Z[173]*Z[100]+Z[176]*Z[97])*Z[48];
  M[13][3] = (Z[61]*Z[203]+Z[70]*Z[209])*Z[76];
  M[13][4] = -(Z[129]*Z[173]+Z[131]*Z[176])*Z[81];
  M[13][5] = (Z[133]*Z[170]-Z[131]*Z[167])*Z[84];
  M[13][6] = -(Z[161]*Z[134]+Z[164]*Z[131])*Z[91];
  M[13][7] = -(Z[92]*Z[209]+Z[93]*Z[203])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M16()
{
  M[16][4] = -(Z[229]*Z[39]+Z[89]*Z[44])*Z[81];
  M[16][5] = (Z[230]*Z[26]-Z[89]*Z[22])*Z[84];
  M[16][6] = -(Z[221]*Z[86]+Z[225]*Z[89])*Z[91];
  M[16][7] = -(Z[93]*Z[65]-Z[232]*Z[56])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M17()
{
  M[17][4] = -(Z[236]*Z[39]+Z[138]*Z[44])*Z[81];
  M[17][5] = (Z[237]*Z[26]-Z[138]*Z[22])*Z[84];
  M[17][6] = -(Z[221]*Z[135]+Z[225]*Z[138])*Z[91];
  M[17][7] = -(Z[93]*Z[120]-Z[232]*Z[112])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M18()
{
  M[18][0] = (Z[139]*Z[221]+Z[141]*Z[225])*Z[18];
  M[18][1] = -(Z[227]*Z[149]-Z[141]*Z[144])*Z[31];
  M[18][2] = (Z[39]*Z[241]+Z[44]*Z[141])*Z[48];
  M[18][3] = (Z[244]*Z[69]-Z[232]*Z[52])*Z[76];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M19()
{
  M[19][0] = (Z[153]*Z[221]+Z[155]*Z[225])*Z[18];
  M[19][1] = -(Z[234]*Z[149]-Z[155]*Z[144])*Z[31];
  M[19][2] = (Z[39]*Z[250]+Z[44]*Z[155])*Z[48];
  M[19][3] = (Z[244]*Z[124]-Z[232]*Z[108])*Z[76];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M28()
{
  M[28][4] = -(Z[228]*Z[173]+Z[89]*Z[176])*Z[81];
  M[28][5] = (Z[231]*Z[170]-Z[89]*Z[167])*Z[84];
  M[28][6] = -(Z[258]*Z[88]+Z[260]*Z[89])*Z[91];
  M[28][7] = -(Z[93]*Z[188]-Z[232]*Z[182])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M29()
{
  M[29][4] = -(Z[235]*Z[173]+Z[138]*Z[176])*Z[81];
  M[29][5] = (Z[238]*Z[170]-Z[138]*Z[167])*Z[84];
  M[29][6] = -(Z[258]*Z[137]+Z[260]*Z[138])*Z[91];
  M[29][7] = -(Z[93]*Z[206]-Z[232]*Z[200])*Z[94];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M30()
{
  M[30][0] = (Z[140]*Z[258]+Z[141]*Z[260])*Z[18];
  M[30][1] = -(Z[226]*Z[217]-Z[141]*Z[214])*Z[31];
  M[30][2] = (Z[173]*Z[239]+Z[176]*Z[141])*Z[48];
  M[30][3] = (Z[244]*Z[191]-Z[232]*Z[179])*Z[76];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M31()
{
  M[31][0] = (Z[154]*Z[258]+Z[155]*Z[260])*Z[18];
  M[31][1] = -(Z[233]*Z[217]-Z[155]*Z[214])*Z[31];
  M[31][2] = (Z[173]*Z[248]+Z[176]*Z[155])*Z[48];
  M[31][3] = (Z[244]*Z[209]-Z[232]*Z[197])*Z[76];
}

void V2_4__d__d__em__ep__d__d__S4_1::Calculate_M32()
{
  M[32][0] = (Z[262]*Z[9]+Z[45]*Z[14])*Z[18];
  M[32][1] = -(Z[263]*Z[26]-Z[45]*Z[22])*Z[31];
  M[32][2] = (Z[268]*Z[34]+Z[272]*Z[45])*Z[48];
  M[32][3] = (Z[70]*Z[74]-Z[273]*Z[56])*Z[76];
}

