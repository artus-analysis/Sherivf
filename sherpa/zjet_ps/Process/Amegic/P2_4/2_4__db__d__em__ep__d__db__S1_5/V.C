#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__db__d__em__ep__d__db__S1_5(Basic_Sfuncs* bs) {
  return new V2_4__db__d__em__ep__d__db__S1_5(bs);
}

V2_4__db__d__em__ep__d__db__S1_5::V2_4__db__d__em__ep__d__db__S1_5(Basic_Sfuncs* _BS) :
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

V2_4__db__d__em__ep__d__db__S1_5::~V2_4__db__d__em__ep__d__db__S1_5()
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

Complex V2_4__db__d__em__ep__d__db__S1_5::Evaluate(int m,int n)
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
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
    case 32: Calculate_M32(); break;
    case 33: Calculate_M33(); break;
    case 44: Calculate_M44(); break;
    case 45: Calculate_M45(); break;
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

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M0()
{
  M[0][0] = -(Z[14]*Z[10]-Z[8]*Z[1])*Z[21];
  M[0][1] = (Z[28]*Z[27]+Z[1]*Z[32])*Z[35];
  M[0][2] = -(Z[1]*Z[39]+Z[44]*Z[43])*Z[48];
  M[0][3] = -(Z[62]*Z[61]-Z[53]*Z[52])*Z[76];
  M[0][4] = -(Z[78]*Z[27]+Z[79]*Z[32])*Z[81];
  M[0][5] = (Z[82]*Z[14]-Z[79]*Z[8])*Z[84];
  M[0][6] = (Z[61]*Z[85]-Z[52]*Z[86])*Z[88];
  M[0][7] = (Z[79]*Z[39]+Z[90]*Z[43])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M1()
{
  M[1][0] = -(Z[14]*Z[97]-Z[8]*Z[95])*Z[21];
  M[1][1] = (Z[102]*Z[27]+Z[95]*Z[32])*Z[35];
  M[1][2] = -(Z[95]*Z[39]+Z[103]*Z[43])*Z[48];
  M[1][3] = -(Z[62]*Z[116]-Z[53]*Z[108])*Z[76];
  M[1][4] = -(Z[130]*Z[27]+Z[131]*Z[32])*Z[81];
  M[1][5] = (Z[132]*Z[14]-Z[131]*Z[8])*Z[84];
  M[1][6] = (Z[116]*Z[85]-Z[108]*Z[86])*Z[88];
  M[1][7] = (Z[131]*Z[39]+Z[135]*Z[43])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M2()
{
  M[2][0] = -(Z[146]*Z[18]-Z[141]*Z[9])*Z[21];
  M[2][1] = (Z[148]*Z[27]+Z[9]*Z[32])*Z[35];
  M[2][2] = -(Z[9]*Z[39]+Z[149]*Z[43])*Z[48];
  M[2][3] = -(Z[151]*Z[74]-Z[53]*Z[57])*Z[76];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M3()
{
  M[3][0] = -(Z[146]*Z[100]-Z[141]*Z[96])*Z[21];
  M[3][1] = (Z[156]*Z[27]+Z[96]*Z[32])*Z[35];
  M[3][2] = -(Z[96]*Z[39]+Z[157]*Z[43])*Z[48];
  M[3][3] = -(Z[151]*Z[128]-Z[53]*Z[112])*Z[76];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M12()
{
  M[12][0] = -(Z[167]*Z[16]-Z[164]*Z[1])*Z[21];
  M[12][1] = (Z[23]*Z[170]+Z[1]*Z[173])*Z[35];
  M[12][2] = -(Z[1]*Z[176]+Z[46]*Z[179])*Z[48];
  M[12][3] = -(Z[62]*Z[188]-Z[53]*Z[182])*Z[76];
  M[12][4] = -(Z[77]*Z[170]+Z[79]*Z[173])*Z[81];
  M[12][5] = (Z[83]*Z[167]-Z[79]*Z[164])*Z[84];
  M[12][6] = (Z[188]*Z[85]-Z[182]*Z[86])*Z[88];
  M[12][7] = (Z[79]*Z[176]+Z[92]*Z[179])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M13()
{
  M[13][0] = -(Z[167]*Z[99]-Z[164]*Z[95])*Z[21];
  M[13][1] = (Z[101]*Z[170]+Z[95]*Z[173])*Z[35];
  M[13][2] = -(Z[95]*Z[176]+Z[104]*Z[179])*Z[48];
  M[13][3] = -(Z[62]*Z[206]-Z[53]*Z[200])*Z[76];
  M[13][4] = -(Z[129]*Z[170]+Z[131]*Z[173])*Z[81];
  M[13][5] = (Z[133]*Z[167]-Z[131]*Z[164])*Z[84];
  M[13][6] = (Z[206]*Z[85]-Z[200]*Z[86])*Z[88];
  M[13][7] = (Z[131]*Z[176]+Z[137]*Z[179])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M14()
{
  M[14][0] = -(Z[220]*Z[15]-Z[217]*Z[9])*Z[21];
  M[14][1] = (Z[147]*Z[170]+Z[9]*Z[173])*Z[35];
  M[14][2] = -(Z[9]*Z[176]+Z[150]*Z[179])*Z[48];
  M[14][3] = -(Z[151]*Z[197]-Z[53]*Z[185])*Z[76];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M15()
{
  M[15][0] = -(Z[220]*Z[98]-Z[217]*Z[96])*Z[21];
  M[15][1] = (Z[155]*Z[170]+Z[96]*Z[173])*Z[35];
  M[15][2] = -(Z[96]*Z[176]+Z[158]*Z[179])*Z[48];
  M[15][3] = -(Z[151]*Z[215]-Z[53]*Z[203])*Z[76];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M18()
{
  M[18][4] = -(Z[152]*Z[224]+Z[154]*Z[228])*Z[81];
  M[18][5] = (Z[233]*Z[146]-Z[154]*Z[141])*Z[84];
  M[18][6] = (Z[61]*Z[242]+Z[70]*Z[151])*Z[88];
  M[18][7] = (Z[154]*Z[39]+Z[244]*Z[43])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M19()
{
  M[19][4] = -(Z[159]*Z[224]+Z[161]*Z[228])*Z[81];
  M[19][5] = (Z[238]*Z[146]-Z[161]*Z[141])*Z[84];
  M[19][6] = (Z[116]*Z[242]+Z[124]*Z[151])*Z[88];
  M[19][7] = (Z[161]*Z[39]+Z[252]*Z[43])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M30()
{
  M[30][4] = -(Z[153]*Z[258]+Z[154]*Z[260])*Z[81];
  M[30][5] = (Z[232]*Z[220]-Z[154]*Z[217])*Z[84];
  M[30][6] = (Z[188]*Z[242]+Z[194]*Z[151])*Z[88];
  M[30][7] = (Z[154]*Z[176]+Z[246]*Z[179])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M31()
{
  M[31][4] = -(Z[160]*Z[258]+Z[161]*Z[260])*Z[81];
  M[31][5] = (Z[237]*Z[220]-Z[161]*Z[217])*Z[84];
  M[31][6] = (Z[206]*Z[242]+Z[212]*Z[151])*Z[88];
  M[31][7] = (Z[161]*Z[176]+Z[254]*Z[179])*Z[94];
}

void V2_4__db__d__em__ep__d__db__S1_5::Calculate_M32()
{
  M[32][4] = -(Z[272]*Z[27]+Z[89]*Z[32])*Z[81];
  M[32][5] = (Z[273]*Z[14]-Z[89]*Z[8])*Z[84];
  M[32][6] = (Z[66]*Z[85]+Z[74]*Z[275])*Z[88];
  M[32][7] = (Z[89]*Z[265]+Z[93]*Z[270])*Z[94];
}

