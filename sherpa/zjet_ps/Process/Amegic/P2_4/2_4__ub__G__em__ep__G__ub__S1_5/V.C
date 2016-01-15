#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__G__em__ep__G__ub__S1_5(Basic_Sfuncs* bs) {
  return new V2_4__ub__G__em__ep__G__ub__S1_5(bs);
}

V2_4__ub__G__em__ep__G__ub__S1_5::V2_4__ub__G__em__ep__G__ub__S1_5(Basic_Sfuncs* _BS) :
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

V2_4__ub__G__em__ep__G__ub__S1_5::~V2_4__ub__G__em__ep__G__ub__S1_5()
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

Complex V2_4__ub__G__em__ep__G__ub__S1_5::Evaluate(int m,int n)
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

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M0()
{
  M[0][0] = -(Z[19]*Z[18]-Z[46]*Z[45])*Z[62];
  M[0][1] = (Z[19]*Z[74]-Z[46]*Z[79])*Z[82];
  M[0][2] = Z[114]*Z[1]*Z[98];
  M[0][3] = -(Z[123]*Z[8]+Z[127]*Z[69]-Z[125]*Z[36])*Z[129];
  M[0][4] = -(Z[133]*Z[86]+Z[141]*Z[92])*Z[154];
  M[0][5] = Z[172]*Z[167]*Z[166];
  M[0][6] = (Z[63]*Z[173]+Z[65]*Z[178])*Z[182];
  M[0][7] = -(Z[63]*Z[187]+Z[65]*Z[200])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M1()
{
  M[1][0] = -(Z[19]*Z[211]-Z[46]*Z[213])*Z[62];
  M[1][1] = (Z[19]*Z[215]-Z[46]*Z[217])*Z[82];
  M[1][2] = Z[114]*Z[1]*Z[105];
  M[1][3] = -(Z[123]*Z[12]+Z[127]*Z[196]-Z[125]*Z[40])*Z[129];
  M[1][4] = -(Z[221]*Z[86]+Z[227]*Z[92])*Z[154];
  M[1][5] = Z[172]*Z[237]*Z[166];
  M[1][6] = (Z[63]*Z[239]+Z[65]*Z[241])*Z[182];
  M[1][7] = -(Z[63]*Z[243]+Z[65]*Z[245])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M2()
{
  M[2][0] = -(Z[247]*Z[18]-Z[248]*Z[45])*Z[62];
  M[2][1] = (Z[247]*Z[74]-Z[248]*Z[79])*Z[82];
  M[2][2] = Z[114]*Z[1]*Z[255];
  M[2][3] = -(Z[273]*Z[8]+Z[275]*Z[69]-Z[274]*Z[36])*Z[129];
  M[2][4] = -(Z[276]*Z[86]+Z[278]*Z[92])*Z[154];
  M[2][5] = Z[172]*Z[283]*Z[166];
  M[2][6] = (Z[63]*Z[285]+Z[65]*Z[290])*Z[182];
  M[2][7] = -(Z[63]*Z[293]+Z[65]*Z[295])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M3()
{
  M[3][0] = -(Z[247]*Z[211]-Z[248]*Z[213])*Z[62];
  M[3][1] = (Z[247]*Z[215]-Z[248]*Z[217])*Z[82];
  M[3][2] = Z[114]*Z[1]*Z[262];
  M[3][3] = -(Z[273]*Z[12]+Z[275]*Z[196]-Z[274]*Z[40])*Z[129];
  M[3][4] = -(Z[297]*Z[86]+Z[299]*Z[92])*Z[154];
  M[3][5] = Z[172]*Z[303]*Z[166];
  M[3][6] = (Z[63]*Z[305]+Z[65]*Z[307])*Z[182];
  M[3][7] = -(Z[63]*Z[309]+Z[65]*Z[311])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M12()
{
  M[12][0] = -(Z[19]*Z[322]-Z[46]*Z[342])*Z[62];
  M[12][1] = (Z[19]*Z[359]-Z[46]*Z[361])*Z[82];
  M[12][2] = Z[114]*Z[1]*Z[369];
  M[12][3] = -(Z[123]*Z[315]+Z[127]*Z[355]-Z[125]*Z[335])*Z[129];
  M[12][4] = -(Z[133]*Z[365]+Z[149]*Z[368])*Z[154];
  M[12][5] = Z[172]*Z[167]*Z[374];
  M[12][6] = (Z[63]*Z[375]+Z[65]*Z[377])*Z[182];
  M[12][7] = -(Z[63]*Z[382]+Z[65]*Z[392])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M13()
{
  M[13][0] = -(Z[19]*Z[399]-Z[46]*Z[401])*Z[62];
  M[13][1] = (Z[19]*Z[403]-Z[46]*Z[405])*Z[82];
  M[13][2] = Z[114]*Z[1]*Z[370];
  M[13][3] = -(Z[123]*Z[318]+Z[127]*Z[389]-Z[125]*Z[338])*Z[129];
  M[13][4] = -(Z[221]*Z[365]+Z[233]*Z[368])*Z[154];
  M[13][5] = Z[172]*Z[237]*Z[374];
  M[13][6] = (Z[63]*Z[407]+Z[65]*Z[409])*Z[182];
  M[13][7] = -(Z[63]*Z[411]+Z[65]*Z[413])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M14()
{
  M[14][0] = -(Z[247]*Z[322]-Z[248]*Z[342])*Z[62];
  M[14][1] = (Z[247]*Z[359]-Z[248]*Z[361])*Z[82];
  M[14][2] = Z[114]*Z[1]*Z[415];
  M[14][3] = -(Z[273]*Z[315]+Z[275]*Z[355]-Z[274]*Z[335])*Z[129];
  M[14][4] = -(Z[276]*Z[365]+Z[280]*Z[368])*Z[154];
  M[14][5] = Z[172]*Z[283]*Z[374];
  M[14][6] = (Z[63]*Z[418]+Z[65]*Z[420])*Z[182];
  M[14][7] = -(Z[63]*Z[422]+Z[65]*Z[424])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M15()
{
  M[15][0] = -(Z[247]*Z[399]-Z[248]*Z[401])*Z[62];
  M[15][1] = (Z[247]*Z[403]-Z[248]*Z[405])*Z[82];
  M[15][2] = Z[114]*Z[1]*Z[416];
  M[15][3] = -(Z[273]*Z[318]+Z[275]*Z[389]-Z[274]*Z[338])*Z[129];
  M[15][4] = -(Z[297]*Z[365]+Z[301]*Z[368])*Z[154];
  M[15][5] = Z[172]*Z[303]*Z[374];
  M[15][6] = (Z[63]*Z[426]+Z[65]*Z[428])*Z[182];
  M[15][7] = -(Z[63]*Z[430]+Z[65]*Z[432])*Z[209];
}

void V2_4__ub__G__em__ep__G__ub__S1_5::Calculate_M16()
{
  M[16][0] = -(Z[19]*Z[436]-Z[46]*Z[438])*Z[62];
  M[16][1] = (Z[19]*Z[442]-Z[46]*Z[447])*Z[82];
  M[16][2] = -(Z[435]*Z[109]-Z[434]*Z[98])*Z[114];
  M[16][3] = -(Z[453]*Z[8]+Z[455]*Z[69]-Z[454]*Z[36])*Z[129];
  M[16][4] = -(Z[457]*Z[86]+Z[461]*Z[92])*Z[154];
  M[16][5] = Z[172]*Z[167]*Z[478];
  M[16][6] = Z[182]*Z[440]*Z[173];
  M[16][7] = -Z[209]*Z[440]*Z[187];
}

