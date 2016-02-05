#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__ub__em__ep__G__ub__S0_4(Basic_Sfuncs* bs) {
  return new V2_4__G__ub__em__ep__G__ub__S0_4(bs);
}

V2_4__G__ub__em__ep__G__ub__S0_4::V2_4__G__ub__em__ep__G__ub__S0_4(Basic_Sfuncs* _BS) :
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

V2_4__G__ub__em__ep__G__ub__S0_4::~V2_4__G__ub__em__ep__G__ub__S0_4()
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

Complex V2_4__G__ub__em__ep__G__ub__S0_4::Evaluate(int m,int n)
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

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M0()
{
  M[0][0] = (Z[24]*Z[19]-Z[33]*Z[28])*Z[36];
  M[0][1] = -(Z[33]*Z[40]+Z[49]*Z[44])*Z[57];
  M[0][2] = Z[116]*Z[100]*Z[99];
  M[0][3] = Z[128]*Z[100]*Z[124];
  M[0][4] = -(Z[68]*Z[143]-Z[58]*Z[135])*Z[147];
  M[0][5] = Z[164]*Z[153]*Z[152];
  M[0][6] = -(Z[166]*Z[165]+Z[171]*Z[170])*Z[174];
  M[0][7] = -(Z[166]*Z[183]+Z[171]*Z[204])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M1()
{
  M[1][0] = (Z[224]*Z[19]-Z[226]*Z[28])*Z[36];
  M[1][1] = -(Z[226]*Z[40]+Z[228]*Z[44])*Z[57];
  M[1][2] = Z[116]*Z[100]*Z[236];
  M[1][3] = Z[128]*Z[100]*Z[245];
  M[1][4] = -(Z[233]*Z[143]-Z[231]*Z[135])*Z[147];
  M[1][5] = Z[164]*Z[249]*Z[152];
  M[1][6] = -(Z[166]*Z[252]+Z[171]*Z[256])*Z[174];
  M[1][7] = -(Z[166]*Z[258]+Z[171]*Z[260])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M2()
{
  M[2][2] = -(Z[279]*Z[86]-Z[100]*Z[113])*Z[116];
  M[2][4] = (Z[63]*Z[281]+Z[58]*Z[280])*Z[147];
  M[2][5] = (Z[284]*Z[158]+Z[283]*Z[152])*Z[164];
  M[2][7] = -(Z[166]*Z[287]+Z[171]*Z[289])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M3()
{
  M[3][2] = -(Z[279]*Z[235]-Z[100]*Z[237])*Z[116];
  M[3][4] = (Z[232]*Z[281]+Z[231]*Z[280])*Z[147];
  M[3][5] = (Z[295]*Z[158]+Z[294]*Z[152])*Z[164];
  M[3][7] = -(Z[166]*Z[298]+Z[171]*Z[300])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M12()
{
  M[12][0] = (Z[15]*Z[304]-Z[33]*Z[307])*Z[36];
  M[12][1] = -(Z[33]*Z[310]+Z[55]*Z[313])*Z[57];
  M[12][2] = Z[116]*Z[100]*Z[343];
  M[12][3] = Z[128]*Z[100]*Z[355];
  M[12][4] = -(Z[68]*Z[358]-Z[58]*Z[356])*Z[147];
  M[12][5] = Z[164]*Z[153]*Z[359];
  M[12][6] = -(Z[166]*Z[362]+Z[171]*Z[363])*Z[174];
  M[12][7] = -(Z[166]*Z[370]+Z[171]*Z[386])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M13()
{
  M[13][0] = (Z[222]*Z[304]-Z[226]*Z[307])*Z[36];
  M[13][1] = -(Z[226]*Z[310]+Z[230]*Z[313])*Z[57];
  M[13][2] = Z[116]*Z[100]*Z[398];
  M[13][3] = Z[128]*Z[100]*Z[401];
  M[13][4] = -(Z[233]*Z[358]-Z[231]*Z[356])*Z[147];
  M[13][5] = Z[164]*Z[249]*Z[359];
  M[13][6] = -(Z[166]*Z[402]+Z[171]*Z[403])*Z[174];
  M[13][7] = -(Z[166]*Z[404]+Z[171]*Z[406])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M14()
{
  M[14][2] = -(Z[279]*Z[333]-Z[100]*Z[353])*Z[116];
  M[14][4] = (Z[63]*Z[414]+Z[58]*Z[413])*Z[147];
  M[14][5] = (Z[284]*Z[360]+Z[283]*Z[359])*Z[164];
  M[14][7] = -(Z[166]*Z[418]+Z[171]*Z[420])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M15()
{
  M[15][2] = -(Z[279]*Z[397]-Z[100]*Z[399])*Z[116];
  M[15][4] = (Z[232]*Z[414]+Z[231]*Z[413])*Z[147];
  M[15][5] = (Z[295]*Z[360]+Z[294]*Z[359])*Z[164];
  M[15][7] = -(Z[166]*Z[424]+Z[171]*Z[426])*Z[217];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M16()
{
  M[16][0] = (Z[434]*Z[19]-Z[436]*Z[28])*Z[36];
  M[16][1] = -(Z[436]*Z[40]+Z[438]*Z[44])*Z[57];
  M[16][2] = -(Z[441]*Z[73]-Z[442]*Z[99])*Z[116];
  M[16][3] = -(Z[441]*Z[120]-Z[442]*Z[124])*Z[128];
  M[16][4] = -(Z[68]*Z[457]-Z[58]*Z[449])*Z[147];
  M[16][5] = Z[164]*Z[153]*Z[465];
  M[16][6] = -Z[174]*Z[474]*Z[165];
  M[16][7] = -Z[217]*Z[474]*Z[183];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M17()
{
  M[17][0] = (Z[477]*Z[19]-Z[478]*Z[28])*Z[36];
  M[17][1] = -(Z[478]*Z[40]+Z[479]*Z[44])*Z[57];
  M[17][2] = -(Z[441]*Z[234]-Z[442]*Z[236])*Z[116];
  M[17][3] = -(Z[441]*Z[241]-Z[442]*Z[245])*Z[128];
  M[17][4] = -(Z[233]*Z[457]-Z[231]*Z[449])*Z[147];
  M[17][5] = Z[164]*Z[249]*Z[465];
  M[17][6] = -Z[174]*Z[474]*Z[252];
  M[17][7] = -Z[217]*Z[474]*Z[258];
}

void V2_4__G__ub__em__ep__G__ub__S0_4::Calculate_M18()
{
  M[18][2] = Z[116]*Z[442]*Z[113];
  M[18][4] = (Z[63]*Z[485]+Z[58]*Z[484])*Z[147];
  M[18][5] = (Z[284]*Z[470]+Z[283]*Z[465])*Z[164];
  M[18][7] = -Z[217]*Z[474]*Z[287];
}

