#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_4_16_10_564_64_18_0(Basic_Sfuncs* bs) {
  return new VP2_4_16_10_564_64_18_0(bs);
}

VP2_4_16_10_564_64_18_0::VP2_4_16_10_564_64_18_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[564];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

VP2_4_16_10_564_64_18_0::~VP2_4_16_10_564_64_18_0()
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

Complex VP2_4_16_10_564_64_18_0::Evaluate(int m,int n)
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

void VP2_4_16_10_564_64_18_0::Calculate_M0()
{
  M[0][0] = Z[61]*Z[45]*Z[44];
  M[0][1] = Z[86]*Z[45]*Z[81];
  M[0][2] = -Z[118]*Z[1]*Z[102];
  M[0][3] = (Z[134]*Z[133]-Z[124]*Z[123])*Z[138];
  M[0][4] = (Z[147]*Z[146]-Z[142]*Z[141])*Z[150];
  M[0][5] = (Z[147]*Z[180]-Z[142]*Z[159])*Z[193];
  M[0][6] = -(Z[205]*Z[93]+Z[208]*Z[99])*Z[210];
  M[0][7] = (Z[213]*Z[71]-Z[208]*Z[66])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M1()
{
  M[1][0] = Z[61]*Z[45]*Z[222];
  M[1][1] = Z[86]*Z[45]*Z[234];
  M[1][2] = -Z[118]*Z[218]*Z[102];
  M[1][3] = (Z[240]*Z[133]-Z[238]*Z[123])*Z[138];
  M[1][4] = (Z[147]*Z[247]-Z[142]*Z[243])*Z[150];
  M[1][5] = (Z[147]*Z[251]-Z[142]*Z[249])*Z[193];
  M[1][6] = -(Z[257]*Z[93]+Z[258]*Z[99])*Z[210];
  M[1][7] = (Z[259]*Z[71]-Z[258]*Z[66])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M2()
{
  M[2][0] = Z[61]*Z[45]*Z[265];
  M[2][2] = -(Z[262]*Z[109]+Z[261]*Z[102])*Z[118];
  M[2][3] = -(Z[130]*Z[278]+Z[124]*Z[277])*Z[138];
  M[2][5] = -Z[193]*Z[142]*Z[168];
}

void VP2_4_16_10_564_64_18_0::Calculate_M3()
{
  M[3][0] = Z[61]*Z[45]*Z[293];
  M[3][2] = -(Z[290]*Z[109]+Z[289]*Z[102])*Z[118];
  M[3][3] = -(Z[239]*Z[278]+Z[238]*Z[277])*Z[138];
  M[3][5] = -Z[193]*Z[142]*Z[250];
}

void VP2_4_16_10_564_64_18_0::Calculate_M12()
{
  M[12][0] = Z[61]*Z[45]*Z[329];
  M[12][1] = Z[86]*Z[45]*Z[347];
  M[12][2] = -Z[118]*Z[1]*Z[354];
  M[12][3] = (Z[134]*Z[359]-Z[124]*Z[357])*Z[138];
  M[12][4] = (Z[147]*Z[361]-Z[142]*Z[360])*Z[150];
  M[12][5] = (Z[147]*Z[384]-Z[142]*Z[368])*Z[193];
  M[12][6] = -(Z[202]*Z[350]+Z[208]*Z[353])*Z[210];
  M[12][7] = (Z[216]*Z[345]-Z[208]*Z[342])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M13()
{
  M[13][0] = Z[61]*Z[45]*Z[396];
  M[13][1] = Z[86]*Z[45]*Z[399];
  M[13][2] = -Z[118]*Z[218]*Z[354];
  M[13][3] = (Z[240]*Z[359]-Z[238]*Z[357])*Z[138];
  M[13][4] = (Z[147]*Z[401]-Z[142]*Z[400])*Z[150];
  M[13][5] = (Z[147]*Z[404]-Z[142]*Z[402])*Z[193];
  M[13][6] = -(Z[256]*Z[350]+Z[258]*Z[353])*Z[210];
  M[13][7] = (Z[260]*Z[345]-Z[258]*Z[342])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M14()
{
  M[14][0] = Z[61]*Z[45]*Z[408];
  M[14][2] = -(Z[262]*Z[355]+Z[261]*Z[354])*Z[118];
  M[14][3] = -(Z[130]*Z[418]+Z[124]*Z[417])*Z[138];
  M[14][5] = -Z[193]*Z[142]*Z[375];
}

void VP2_4_16_10_564_64_18_0::Calculate_M15()
{
  M[15][0] = Z[61]*Z[45]*Z[422];
  M[15][2] = -(Z[290]*Z[355]+Z[289]*Z[354])*Z[118];
  M[15][3] = -(Z[239]*Z[418]+Z[238]*Z[417])*Z[138];
  M[15][5] = -Z[193]*Z[142]*Z[403];
}

void VP2_4_16_10_564_64_18_0::Calculate_M16()
{
  M[16][0] = (Z[426]*Z[18]+Z[427]*Z[44])*Z[61];
  M[16][1] = (Z[426]*Z[74]+Z[427]*Z[81])*Z[86];
  M[16][2] = -Z[118]*Z[1]*Z[434];
  M[16][3] = (Z[134]*Z[461]-Z[124]*Z[453])*Z[138];
  M[16][4] = -Z[150]*Z[464]*Z[141];
  M[16][5] = -Z[193]*Z[464]*Z[159];
  M[16][6] = -(Z[469]*Z[93]+Z[470]*Z[99])*Z[210];
  M[16][7] = (Z[471]*Z[71]-Z[470]*Z[66])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M17()
{
  M[17][0] = (Z[426]*Z[220]+Z[427]*Z[222])*Z[61];
  M[17][1] = (Z[426]*Z[227]+Z[427]*Z[234])*Z[86];
  M[17][2] = -Z[118]*Z[218]*Z[434];
  M[17][3] = (Z[240]*Z[461]-Z[238]*Z[453])*Z[138];
  M[17][4] = -Z[150]*Z[464]*Z[243];
  M[17][5] = -Z[193]*Z[464]*Z[249];
  M[17][6] = -(Z[475]*Z[93]+Z[476]*Z[99])*Z[210];
  M[17][7] = (Z[477]*Z[71]-Z[476]*Z[66])*Z[217];
}

void VP2_4_16_10_564_64_18_0::Calculate_M18()
{
  M[18][0] = (Z[426]*Z[263]+Z[427]*Z[265])*Z[61];
  M[18][2] = -(Z[262]*Z[441]+Z[261]*Z[434])*Z[118];
  M[18][3] = -(Z[130]*Z[480]+Z[124]*Z[479])*Z[138];
  M[18][5] = (Z[482]*Z[192]-Z[464]*Z[168])*Z[193];
}

