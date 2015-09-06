#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_4_16_10_565_64_18_0(Basic_Sfuncs* bs) {
  return new VP2_4_16_10_565_64_18_0(bs);
}

VP2_4_16_10_565_64_18_0::VP2_4_16_10_565_64_18_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[565];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

VP2_4_16_10_565_64_18_0::~VP2_4_16_10_565_64_18_0()
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

Complex VP2_4_16_10_565_64_18_0::Evaluate(int m,int n)
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

void VP2_4_16_10_565_64_18_0::Calculate_M0()
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

void VP2_4_16_10_565_64_18_0::Calculate_M1()
{
  M[1][0] = Z[61]*Z[45]*Z[223];
  M[1][1] = Z[86]*Z[45]*Z[235];
  M[1][2] = -Z[118]*Z[218]*Z[102];
  M[1][3] = (Z[241]*Z[133]-Z[239]*Z[123])*Z[138];
  M[1][4] = (Z[147]*Z[248]-Z[142]*Z[244])*Z[150];
  M[1][5] = (Z[147]*Z[252]-Z[142]*Z[250])*Z[193];
  M[1][6] = -(Z[258]*Z[93]+Z[259]*Z[99])*Z[210];
  M[1][7] = (Z[260]*Z[71]-Z[259]*Z[66])*Z[217];
}

void VP2_4_16_10_565_64_18_0::Calculate_M2()
{
  M[2][0] = Z[61]*Z[45]*Z[266];
  M[2][2] = -(Z[263]*Z[109]+Z[262]*Z[102])*Z[118];
  M[2][3] = -(Z[130]*Z[279]+Z[124]*Z[278])*Z[138];
  M[2][5] = -Z[193]*Z[142]*Z[168];
}

void VP2_4_16_10_565_64_18_0::Calculate_M3()
{
  M[3][0] = Z[61]*Z[45]*Z[294];
  M[3][2] = -(Z[291]*Z[109]+Z[290]*Z[102])*Z[118];
  M[3][3] = -(Z[240]*Z[279]+Z[239]*Z[278])*Z[138];
  M[3][5] = -Z[193]*Z[142]*Z[251];
}

void VP2_4_16_10_565_64_18_0::Calculate_M12()
{
  M[12][0] = Z[61]*Z[45]*Z[330];
  M[12][1] = Z[86]*Z[45]*Z[348];
  M[12][2] = -Z[118]*Z[1]*Z[355];
  M[12][3] = (Z[134]*Z[360]-Z[124]*Z[358])*Z[138];
  M[12][4] = (Z[147]*Z[362]-Z[142]*Z[361])*Z[150];
  M[12][5] = (Z[147]*Z[385]-Z[142]*Z[369])*Z[193];
  M[12][6] = -(Z[202]*Z[351]+Z[208]*Z[354])*Z[210];
  M[12][7] = (Z[216]*Z[346]-Z[208]*Z[343])*Z[217];
}

void VP2_4_16_10_565_64_18_0::Calculate_M13()
{
  M[13][0] = Z[61]*Z[45]*Z[397];
  M[13][1] = Z[86]*Z[45]*Z[400];
  M[13][2] = -Z[118]*Z[218]*Z[355];
  M[13][3] = (Z[241]*Z[360]-Z[239]*Z[358])*Z[138];
  M[13][4] = (Z[147]*Z[402]-Z[142]*Z[401])*Z[150];
  M[13][5] = (Z[147]*Z[405]-Z[142]*Z[403])*Z[193];
  M[13][6] = -(Z[257]*Z[351]+Z[259]*Z[354])*Z[210];
  M[13][7] = (Z[261]*Z[346]-Z[259]*Z[343])*Z[217];
}

void VP2_4_16_10_565_64_18_0::Calculate_M14()
{
  M[14][0] = Z[61]*Z[45]*Z[409];
  M[14][2] = -(Z[263]*Z[356]+Z[262]*Z[355])*Z[118];
  M[14][3] = -(Z[130]*Z[419]+Z[124]*Z[418])*Z[138];
  M[14][5] = -Z[193]*Z[142]*Z[376];
}

void VP2_4_16_10_565_64_18_0::Calculate_M15()
{
  M[15][0] = Z[61]*Z[45]*Z[423];
  M[15][2] = -(Z[291]*Z[356]+Z[290]*Z[355])*Z[118];
  M[15][3] = -(Z[240]*Z[419]+Z[239]*Z[418])*Z[138];
  M[15][5] = -Z[193]*Z[142]*Z[404];
}

void VP2_4_16_10_565_64_18_0::Calculate_M16()
{
  M[16][0] = (Z[427]*Z[18]+Z[428]*Z[44])*Z[61];
  M[16][1] = (Z[427]*Z[74]+Z[428]*Z[81])*Z[86];
  M[16][2] = -Z[118]*Z[1]*Z[435];
  M[16][3] = (Z[134]*Z[462]-Z[124]*Z[454])*Z[138];
  M[16][4] = -Z[150]*Z[465]*Z[141];
  M[16][5] = -Z[193]*Z[465]*Z[159];
  M[16][6] = -(Z[470]*Z[93]+Z[471]*Z[99])*Z[210];
  M[16][7] = (Z[472]*Z[71]-Z[471]*Z[66])*Z[217];
}

void VP2_4_16_10_565_64_18_0::Calculate_M17()
{
  M[17][0] = (Z[427]*Z[221]+Z[428]*Z[223])*Z[61];
  M[17][1] = (Z[427]*Z[228]+Z[428]*Z[235])*Z[86];
  M[17][2] = -Z[118]*Z[218]*Z[435];
  M[17][3] = (Z[241]*Z[462]-Z[239]*Z[454])*Z[138];
  M[17][4] = -Z[150]*Z[465]*Z[244];
  M[17][5] = -Z[193]*Z[465]*Z[250];
  M[17][6] = -(Z[476]*Z[93]+Z[477]*Z[99])*Z[210];
  M[17][7] = (Z[478]*Z[71]-Z[477]*Z[66])*Z[217];
}

void VP2_4_16_10_565_64_18_0::Calculate_M18()
{
  M[18][0] = (Z[427]*Z[264]+Z[428]*Z[266])*Z[61];
  M[18][2] = -(Z[263]*Z[442]+Z[262]*Z[435])*Z[118];
  M[18][3] = -(Z[130]*Z[481]+Z[124]*Z[480])*Z[138];
  M[18][5] = (Z[483]*Z[192]-Z[465]*Z[168])*Z[193];
}

