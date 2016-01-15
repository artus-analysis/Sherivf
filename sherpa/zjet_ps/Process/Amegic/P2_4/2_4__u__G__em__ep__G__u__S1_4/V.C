#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__G__em__ep__G__u__S1_4(Basic_Sfuncs* bs) {
  return new V2_4__u__G__em__ep__G__u__S1_4(bs);
}

V2_4__u__G__em__ep__G__u__S1_4::V2_4__u__G__em__ep__G__u__S1_4(Basic_Sfuncs* _BS) :
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

V2_4__u__G__em__ep__G__u__S1_4::~V2_4__u__G__em__ep__G__u__S1_4()
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

Complex V2_4__u__G__em__ep__G__u__S1_4::Evaluate(int m,int n)
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

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M0()
{
  M[0][0] = Z[62]*Z[46]*Z[45];
  M[0][1] = -Z[94]*Z[13]*Z[89];
  M[0][2] = -Z[116]*Z[46]*Z[112];
  M[0][3] = -(Z[134]*Z[70]+Z[142]*Z[76])*Z[148];
  M[0][4] = -(Z[155]*Z[36]+Z[152]*Z[8]-Z[150]*Z[98])*Z[156];
  M[0][5] = -(Z[111]*Z[161]-Z[110]*Z[158])*Z[165];
  M[0][6] = (Z[178]*Z[177]-Z[167]*Z[166])*Z[182];
  M[0][7] = (Z[111]*Z[203]-Z[110]*Z[190])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M1()
{
  M[1][0] = Z[62]*Z[46]*Z[214];
  M[1][1] = -Z[94]*Z[210]*Z[89];
  M[1][2] = -Z[116]*Z[46]*Z[218];
  M[1][3] = -(Z[228]*Z[70]+Z[234]*Z[76])*Z[148];
  M[1][4] = -(Z[155]*Z[40]+Z[152]*Z[12]-Z[150]*Z[186])*Z[156];
  M[1][5] = -(Z[111]*Z[240]-Z[110]*Z[238])*Z[165];
  M[1][6] = (Z[242]*Z[177]-Z[167]*Z[174])*Z[182];
  M[1][7] = (Z[111]*Z[245]-Z[110]*Z[243])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M2()
{
  M[2][0] = Z[62]*Z[46]*Z[252];
  M[2][1] = -Z[94]*Z[248]*Z[89];
  M[2][2] = -Z[116]*Z[46]*Z[263];
  M[2][3] = -(Z[274]*Z[70]+Z[278]*Z[76])*Z[148];
  M[2][4] = -(Z[283]*Z[36]+Z[282]*Z[8]-Z[281]*Z[98])*Z[156];
  M[2][5] = -(Z[262]*Z[161]-Z[261]*Z[158])*Z[165];
  M[2][6] = (Z[178]*Z[294]-Z[167]*Z[284])*Z[182];
  M[2][7] = (Z[262]*Z[203]-Z[261]*Z[190])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M3()
{
  M[3][0] = Z[62]*Z[46]*Z[301];
  M[3][1] = -Z[94]*Z[297]*Z[89];
  M[3][2] = -Z[116]*Z[46]*Z[305];
  M[3][3] = -(Z[309]*Z[70]+Z[311]*Z[76])*Z[148];
  M[3][4] = -(Z[283]*Z[40]+Z[282]*Z[12]-Z[281]*Z[186])*Z[156];
  M[3][5] = -(Z[262]*Z[240]-Z[261]*Z[238])*Z[165];
  M[3][6] = (Z[242]*Z[294]-Z[167]*Z[291])*Z[182];
  M[3][7] = (Z[262]*Z[245]-Z[261]*Z[243])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M12()
{
  M[12][0] = Z[62]*Z[46]*Z[342];
  M[12][1] = -Z[94]*Z[13]*Z[361];
  M[12][2] = -Z[116]*Z[46]*Z[370];
  M[12][3] = -(Z[126]*Z[355]+Z[142]*Z[358])*Z[148];
  M[12][4] = -(Z[155]*Z[335]+Z[152]*Z[315]-Z[150]*Z[364])*Z[156];
  M[12][5] = -(Z[111]*Z[374]-Z[110]*Z[372])*Z[165];
  M[12][6] = (Z[178]*Z[378]-Z[167]*Z[376])*Z[182];
  M[12][7] = (Z[111]*Z[394]-Z[110]*Z[384])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M13()
{
  M[13][0] = Z[62]*Z[46]*Z[401];
  M[13][1] = -Z[94]*Z[210]*Z[361];
  M[13][2] = -Z[116]*Z[46]*Z[405];
  M[13][3] = -(Z[222]*Z[355]+Z[234]*Z[358])*Z[148];
  M[13][4] = -(Z[155]*Z[338]+Z[152]*Z[318]-Z[150]*Z[381])*Z[156];
  M[13][5] = -(Z[111]*Z[409]-Z[110]*Z[407])*Z[165];
  M[13][6] = (Z[242]*Z[378]-Z[167]*Z[377])*Z[182];
  M[13][7] = (Z[111]*Z[413]-Z[110]*Z[411])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M14()
{
  M[14][0] = Z[62]*Z[46]*Z[417];
  M[14][1] = -Z[94]*Z[248]*Z[361];
  M[14][2] = -Z[116]*Z[46]*Z[421];
  M[14][3] = -(Z[270]*Z[355]+Z[278]*Z[358])*Z[148];
  M[14][4] = -(Z[283]*Z[335]+Z[282]*Z[315]-Z[281]*Z[364])*Z[156];
  M[14][5] = -(Z[262]*Z[374]-Z[261]*Z[372])*Z[165];
  M[14][6] = (Z[178]*Z[425]-Z[167]*Z[423])*Z[182];
  M[14][7] = (Z[262]*Z[394]-Z[261]*Z[384])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M15()
{
  M[15][0] = Z[62]*Z[46]*Z[428];
  M[15][1] = -Z[94]*Z[297]*Z[361];
  M[15][2] = -Z[116]*Z[46]*Z[432];
  M[15][3] = -(Z[307]*Z[355]+Z[311]*Z[358])*Z[148];
  M[15][4] = -(Z[283]*Z[338]+Z[282]*Z[318]-Z[281]*Z[381])*Z[156];
  M[15][5] = -(Z[262]*Z[409]-Z[261]*Z[407])*Z[165];
  M[15][6] = (Z[242]*Z[425]-Z[167]*Z[424])*Z[182];
  M[15][7] = (Z[262]*Z[413]-Z[261]*Z[411])*Z[209];
}

void V2_4__u__G__em__ep__G__u__S1_4::Calculate_M16()
{
  M[16][0] = (Z[434]*Z[19]+Z[435]*Z[45])*Z[62];
  M[16][1] = -Z[94]*Z[13]*Z[453];
  M[16][2] = -(Z[434]*Z[106]+Z[435]*Z[112])*Z[116];
  M[16][3] = -(Z[462]*Z[70]+Z[464]*Z[76])*Z[148];
  M[16][4] = -(Z[468]*Z[36]+Z[467]*Z[8]-Z[466]*Z[98])*Z[156];
  M[16][5] = -(Z[111]*Z[473]-Z[110]*Z[471])*Z[165];
  M[16][6] = -Z[182]*Z[475]*Z[166];
  M[16][7] = (Z[111]*Z[479]-Z[110]*Z[477])*Z[209];
}

