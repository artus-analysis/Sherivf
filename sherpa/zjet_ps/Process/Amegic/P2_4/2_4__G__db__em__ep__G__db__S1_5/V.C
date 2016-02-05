#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__db__em__ep__G__db__S1_5(Basic_Sfuncs* bs) {
  return new V2_4__G__db__em__ep__G__db__S1_5(bs);
}

V2_4__G__db__em__ep__G__db__S1_5::V2_4__G__db__em__ep__G__db__S1_5(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[530];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__G__db__em__ep__G__db__S1_5::~V2_4__G__db__em__ep__G__db__S1_5()
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

Complex V2_4__G__db__em__ep__G__db__S1_5::Evaluate(int m,int n)
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

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M0()
{
  M[0][0] = (Z[24]*Z[19]-Z[32]*Z[28])*Z[35];
  M[0][1] = -(Z[32]*Z[39]+Z[47]*Z[43])*Z[54];
  M[0][2] = Z[113]*Z[97]*Z[96];
  M[0][4] = -(Z[65]*Z[139]-Z[55]*Z[131])*Z[143];
  M[0][6] = -(Z[160]*Z[159]+Z[164]*Z[163])*Z[167];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M1()
{
  M[1][0] = (Z[213]*Z[19]-Z[215]*Z[28])*Z[35];
  M[1][1] = -(Z[215]*Z[39]+Z[217]*Z[43])*Z[54];
  M[1][2] = Z[113]*Z[97]*Z[224];
  M[1][3] = Z[124]*Z[97]*Z[233];
  M[1][4] = -Z[143]*Z[221]*Z[139];
  M[1][5] = Z[158]*Z[234]*Z[148];
  M[1][6] = -(Z[160]*Z[236]+Z[164]*Z[240])*Z[167];
  M[1][7] = -(Z[160]*Z[241]+Z[164]*Z[243])*Z[206];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M2()
{
  M[2][2] = -(Z[262]*Z[83]-Z[97]*Z[110])*Z[113];
  M[2][4] = (Z[60]*Z[264]+Z[55]*Z[263])*Z[143];
  M[2][5] = (Z[267]*Z[153]+Z[266]*Z[148])*Z[158];
  M[2][7] = -(Z[160]*Z[270]+Z[164]*Z[272])*Z[206];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M3()
{
  M[3][2] = -(Z[262]*Z[223]-Z[97]*Z[225])*Z[113];
  M[3][4] = Z[143]*Z[220]*Z[264];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M12()
{
  M[12][0] = (Z[15]*Z[281]-Z[32]*Z[284])*Z[35];
  M[12][1] = -(Z[32]*Z[287]+Z[52]*Z[290])*Z[54];
  M[12][2] = Z[113]*Z[97]*Z[320];
  M[12][4] = -(Z[65]*Z[334]-Z[55]*Z[332])*Z[143];
  M[12][6] = -(Z[160]*Z[338]+Z[164]*Z[339])*Z[167];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M13()
{
  M[13][0] = (Z[211]*Z[281]-Z[215]*Z[284])*Z[35];
  M[13][1] = -(Z[215]*Z[287]+Z[219]*Z[290])*Z[54];
  M[13][2] = Z[113]*Z[97]*Z[370];
  M[13][3] = Z[124]*Z[97]*Z[373];
  M[13][4] = -Z[143]*Z[221]*Z[334];
  M[13][5] = Z[158]*Z[234]*Z[335];
  M[13][6] = -(Z[160]*Z[374]+Z[164]*Z[375])*Z[167];
  M[13][7] = -(Z[160]*Z[376]+Z[164]*Z[378])*Z[206];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M14()
{
  M[14][2] = -(Z[262]*Z[310]-Z[97]*Z[330])*Z[113];
  M[14][4] = (Z[60]*Z[386]+Z[55]*Z[385])*Z[143];
  M[14][5] = (Z[267]*Z[336]+Z[266]*Z[335])*Z[158];
  M[14][7] = -(Z[160]*Z[390]+Z[164]*Z[392])*Z[206];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M15()
{
  M[15][2] = -(Z[262]*Z[369]-Z[97]*Z[371])*Z[113];
  M[15][4] = Z[143]*Z[220]*Z[386];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M16()
{
  M[16][0] = (Z[402]*Z[19]-Z[404]*Z[28])*Z[35];
  M[16][1] = -(Z[404]*Z[39]+Z[406]*Z[43])*Z[54];
  M[16][2] = -(Z[409]*Z[70]-Z[410]*Z[96])*Z[113];
  M[16][3] = -Z[124]*Z[409]*Z[117];
  M[16][4] = -(Z[65]*Z[425]-Z[55]*Z[417])*Z[143];
  M[16][6] = -Z[167]*Z[442]*Z[159];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M17()
{
  M[17][0] = (Z[445]*Z[19]-Z[446]*Z[28])*Z[35];
  M[17][1] = -(Z[446]*Z[39]+Z[447]*Z[43])*Z[54];
  M[17][2] = -(Z[409]*Z[222]-Z[410]*Z[224])*Z[113];
  M[17][3] = -(Z[409]*Z[229]-Z[410]*Z[233])*Z[124];
  M[17][4] = -Z[143]*Z[221]*Z[425];
  M[17][5] = Z[158]*Z[234]*Z[433];
  M[17][6] = -Z[167]*Z[442]*Z[236];
  M[17][7] = -Z[206]*Z[442]*Z[241];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M18()
{
  M[18][2] = Z[113]*Z[410]*Z[110];
  M[18][4] = (Z[60]*Z[453]+Z[55]*Z[452])*Z[143];
  M[18][5] = (Z[267]*Z[438]+Z[266]*Z[433])*Z[158];
  M[18][7] = -Z[206]*Z[442]*Z[270];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M19()
{
  M[19][2] = Z[113]*Z[410]*Z[225];
  M[19][4] = Z[143]*Z[220]*Z[453];
}

void V2_4__G__db__em__ep__G__db__S1_5::Calculate_M28()
{
  M[28][0] = (Z[400]*Z[281]-Z[404]*Z[284])*Z[35];
  M[28][1] = -(Z[404]*Z[287]+Z[408]*Z[290])*Z[54];
  M[28][2] = -(Z[409]*Z[300]-Z[410]*Z[320])*Z[113];
  M[28][3] = -Z[124]*Z[409]*Z[331];
  M[28][4] = -(Z[65]*Z[460]-Z[55]*Z[458])*Z[143];
  M[28][6] = -Z[167]*Z[442]*Z[338];
}

