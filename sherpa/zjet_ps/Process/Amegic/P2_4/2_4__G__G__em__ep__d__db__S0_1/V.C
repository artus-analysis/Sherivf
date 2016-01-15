#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__G__em__ep__d__db__S0_1(Basic_Sfuncs* bs) {
  return new V2_4__G__G__em__ep__d__db__S0_1(bs);
}

V2_4__G__G__em__ep__d__db__S0_1::V2_4__G__G__em__ep__d__db__S0_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[544];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__G__G__em__ep__d__db__S0_1::~V2_4__G__G__em__ep__d__db__S0_1()
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

Complex V2_4__G__G__em__ep__d__db__S0_1::Evaluate(int m,int n)
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

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M0()
{
  M[0][0] = (Z[20]*Z[15]+Z[29]*Z[24])*Z[32];
  M[0][1] = -(Z[29]*Z[36]+Z[45]*Z[40])*Z[53];
  M[0][2] = -(Z[68]*Z[67]-Z[61]*Z[60])*Z[73];
  M[0][3] = -Z[128]*Z[113]*Z[112];
  M[0][4] = -Z[140]*Z[113]*Z[136];
  M[0][5] = -(Z[142]*Z[141]-Z[147]*Z[146])*Z[150];
  M[0][6] = -(Z[142]*Z[162]-Z[147]*Z[183])*Z[197];
  M[0][7] = -Z[209]*Z[161]*Z[206];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M1()
{
  M[1][0] = (Z[216]*Z[15]+Z[218]*Z[24])*Z[32];
  M[1][1] = -(Z[218]*Z[36]+Z[220]*Z[40])*Z[53];
  M[1][2] = -(Z[225]*Z[67]-Z[223]*Z[60])*Z[73];
  M[1][3] = -Z[128]*Z[113]*Z[228];
  M[1][4] = -Z[140]*Z[113]*Z[237];
  M[1][5] = -(Z[142]*Z[241]-Z[147]*Z[245])*Z[150];
  M[1][6] = -(Z[142]*Z[250]-Z[147]*Z[252])*Z[197];
  M[1][7] = -Z[209]*Z[249]*Z[206];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M2()
{
  M[2][0] = (Z[258]*Z[15]+Z[260]*Z[24])*Z[32];
  M[2][1] = -(Z[260]*Z[36]+Z[262]*Z[40])*Z[53];
  M[2][2] = -Z[73]*Z[68]*Z[275];
  M[2][3] = -(Z[280]*Z[112]-Z[279]*Z[86])*Z[128];
  M[2][4] = -(Z[280]*Z[136]-Z[279]*Z[132])*Z[140];
  M[2][5] = -Z[150]*Z[281]*Z[141];
  M[2][6] = -Z[197]*Z[281]*Z[162];
  M[2][7] = -(Z[161]*Z[291]-Z[151]*Z[286])*Z[209];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M3()
{
  M[3][0] = (Z[296]*Z[15]+Z[297]*Z[24])*Z[32];
  M[3][1] = -(Z[297]*Z[36]+Z[298]*Z[40])*Z[53];
  M[3][2] = -Z[73]*Z[225]*Z[275];
  M[3][3] = -(Z[280]*Z[228]-Z[279]*Z[226])*Z[128];
  M[3][4] = -(Z[280]*Z[237]-Z[279]*Z[233])*Z[140];
  M[3][5] = -Z[150]*Z[281]*Z[241];
  M[3][6] = -Z[197]*Z[281]*Z[250];
  M[3][7] = -(Z[249]*Z[291]-Z[247]*Z[286])*Z[209];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M12()
{
  M[12][0] = (Z[11]*Z[302]+Z[29]*Z[305])*Z[32];
  M[12][1] = -(Z[29]*Z[308]+Z[51]*Z[311])*Z[53];
  M[12][2] = -(Z[68]*Z[314]-Z[61]*Z[312])*Z[73];
  M[12][3] = -Z[128]*Z[113]*Z[344];
  M[12][4] = -Z[140]*Z[113]*Z[356];
  M[12][5] = -(Z[142]*Z[357]-Z[147]*Z[358])*Z[150];
  M[12][6] = -(Z[142]*Z[365]-Z[147]*Z[381])*Z[197];
  M[12][7] = -Z[209]*Z[161]*Z[392];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M13()
{
  M[13][0] = (Z[214]*Z[302]+Z[218]*Z[305])*Z[32];
  M[13][1] = -(Z[218]*Z[308]+Z[222]*Z[311])*Z[53];
  M[13][2] = -(Z[225]*Z[314]-Z[223]*Z[312])*Z[73];
  M[13][3] = -Z[128]*Z[113]*Z[395];
  M[13][4] = -Z[140]*Z[113]*Z[398];
  M[13][5] = -(Z[142]*Z[399]-Z[147]*Z[400])*Z[150];
  M[13][6] = -(Z[142]*Z[401]-Z[147]*Z[403])*Z[197];
  M[13][7] = -Z[209]*Z[249]*Z[392];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M14()
{
  M[14][0] = (Z[256]*Z[302]+Z[260]*Z[305])*Z[32];
  M[14][1] = -(Z[260]*Z[308]+Z[264]*Z[311])*Z[53];
  M[14][2] = -Z[73]*Z[68]*Z[406];
  M[14][3] = -(Z[280]*Z[344]-Z[279]*Z[324])*Z[128];
  M[14][4] = -(Z[280]*Z[356]-Z[279]*Z[355])*Z[140];
  M[14][5] = -Z[150]*Z[281]*Z[357];
  M[14][6] = -Z[197]*Z[281]*Z[365];
  M[14][7] = -(Z[161]*Z[409]-Z[151]*Z[407])*Z[209];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M15()
{
  M[15][0] = (Z[295]*Z[302]+Z[297]*Z[305])*Z[32];
  M[15][1] = -(Z[297]*Z[308]+Z[299]*Z[311])*Z[53];
  M[15][2] = -Z[73]*Z[225]*Z[406];
  M[15][3] = -(Z[280]*Z[395]-Z[279]*Z[393])*Z[128];
  M[15][4] = -(Z[280]*Z[398]-Z[279]*Z[397])*Z[140];
  M[15][5] = -Z[150]*Z[281]*Z[399];
  M[15][6] = -Z[197]*Z[281]*Z[401];
  M[15][7] = -(Z[249]*Z[409]-Z[247]*Z[407])*Z[209];
}

void V2_4__G__G__em__ep__d__db__S0_1::Calculate_M16()
{
  M[16][2] = Z[73]*Z[61]*Z[427];
  M[16][3] = -(Z[113]*Z[126]-Z[429]*Z[99])*Z[128];
  M[16][6] = -(Z[142]*Z[434]-Z[147]*Z[436])*Z[197];
  M[16][7] = Z[209]*Z[433]*Z[205];
}

