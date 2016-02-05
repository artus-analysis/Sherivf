#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__G__em__ep__d__db(Basic_Sfuncs* bs) {
  return new V2_4__G__G__em__ep__d__db(bs);
}

V2_4__G__G__em__ep__d__db::V2_4__G__G__em__ep__d__db(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[434];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__G__G__em__ep__d__db::~V2_4__G__G__em__ep__d__db()
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

Complex V2_4__G__G__em__ep__d__db::Evaluate(int m,int n)
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

void V2_4__G__G__em__ep__d__db::Calculate_M0()
{
  M[0][0] = (Z[20]*Z[15]+Z[29]*Z[24])*Z[32];
  M[0][1] = -(Z[29]*Z[36]+Z[45]*Z[40])*Z[53];
  M[0][2] = -(Z[68]*Z[67]-Z[61]*Z[60])*Z[73];
  M[0][3] = -Z[128]*Z[113]*Z[112];
  M[0][4] = -Z[136]*Z[113]*Z[132];
  M[0][5] = -(Z[138]*Z[137]-Z[143]*Z[142])*Z[145];
  M[0][6] = -(Z[138]*Z[156]-Z[143]*Z[177])*Z[191];
  M[0][7] = -Z[203]*Z[155]*Z[200];
}

void V2_4__G__G__em__ep__d__db::Calculate_M1()
{
  M[1][2] = -Z[73]*Z[138]*Z[67];
  M[1][3] = -Z[128]*Z[113]*Z[206];
  M[1][4] = -Z[136]*Z[113]*Z[200];
  M[1][5] = -Z[145]*Z[138]*Z[67];
  M[1][6] = -(Z[138]*Z[212]-Z[143]*Z[214])*Z[191];
  M[1][7] = -Z[203]*Z[113]*Z[200];
}

void V2_4__G__G__em__ep__d__db::Calculate_M2()
{
  M[2][2] = -Z[73]*Z[68]*Z[137];
  M[2][3] = -(Z[155]*Z[112]-Z[141]*Z[86])*Z[128];
  M[2][4] = -Z[136]*Z[155]*Z[132];
  M[2][5] = -Z[145]*Z[68]*Z[137];
  M[2][6] = -Z[191]*Z[68]*Z[156];
  M[2][7] = -Z[203]*Z[155]*Z[132];
}

void V2_4__G__G__em__ep__d__db::Calculate_M3()
{
  M[3][0] = (Z[20]*Z[15]+Z[29]*Z[24])*Z[32];
  M[3][1] = -(Z[29]*Z[36]+Z[45]*Z[40])*Z[53];
  M[3][2] = -Z[73]*Z[138]*Z[137];
  M[3][3] = -(Z[155]*Z[206]-Z[141]*Z[204])*Z[128];
  M[3][4] = -(Z[155]*Z[200]-Z[141]*Z[210])*Z[136];
  M[3][5] = -Z[145]*Z[68]*Z[67];
  M[3][6] = -Z[191]*Z[68]*Z[212];
  M[3][7] = -(Z[113]*Z[132]-Z[58]*Z[228])*Z[203];
}

void V2_4__G__G__em__ep__d__db::Calculate_M12()
{
  M[12][0] = (Z[11]*Z[235]+Z[29]*Z[238])*Z[32];
  M[12][1] = -(Z[29]*Z[241]+Z[51]*Z[244])*Z[53];
  M[12][2] = -(Z[68]*Z[247]-Z[61]*Z[245])*Z[73];
  M[12][3] = -Z[128]*Z[113]*Z[277];
  M[12][4] = -Z[136]*Z[113]*Z[288];
  M[12][5] = -(Z[138]*Z[289]-Z[143]*Z[290])*Z[145];
  M[12][6] = -(Z[138]*Z[297]-Z[143]*Z[313])*Z[191];
  M[12][7] = -Z[203]*Z[155]*Z[324];
}

void V2_4__G__G__em__ep__d__db::Calculate_M13()
{
  M[13][2] = -Z[73]*Z[138]*Z[247];
  M[13][3] = -Z[128]*Z[113]*Z[327];
  M[13][4] = -Z[136]*Z[113]*Z[324];
  M[13][5] = -Z[145]*Z[138]*Z[247];
  M[13][6] = -(Z[138]*Z[330]-Z[143]*Z[332])*Z[191];
  M[13][7] = -Z[203]*Z[113]*Z[324];
}

void V2_4__G__G__em__ep__d__db::Calculate_M14()
{
  M[14][2] = -Z[73]*Z[68]*Z[289];
  M[14][3] = -(Z[155]*Z[277]-Z[141]*Z[257])*Z[128];
  M[14][4] = -Z[136]*Z[155]*Z[288];
  M[14][5] = -Z[145]*Z[68]*Z[289];
  M[14][6] = -Z[191]*Z[68]*Z[297];
  M[14][7] = -Z[203]*Z[155]*Z[288];
}

void V2_4__G__G__em__ep__d__db::Calculate_M15()
{
  M[15][0] = (Z[11]*Z[235]+Z[29]*Z[238])*Z[32];
  M[15][1] = -(Z[29]*Z[241]+Z[51]*Z[244])*Z[53];
  M[15][2] = -Z[73]*Z[138]*Z[289];
  M[15][3] = -(Z[155]*Z[327]-Z[141]*Z[325])*Z[128];
  M[15][4] = -(Z[155]*Z[324]-Z[141]*Z[329])*Z[136];
  M[15][5] = -Z[145]*Z[68]*Z[247];
  M[15][6] = -Z[191]*Z[68]*Z[330];
  M[15][7] = -(Z[113]*Z[288]-Z[58]*Z[335])*Z[203];
}

void V2_4__G__G__em__ep__d__db::Calculate_M16()
{
  M[16][2] = Z[73]*Z[61]*Z[354];
  M[16][3] = -(Z[113]*Z[126]-Z[211]*Z[99])*Z[128];
  M[16][6] = -(Z[138]*Z[357]-Z[143]*Z[359])*Z[191];
  M[16][7] = Z[203]*Z[223]*Z[199];
}

void V2_4__G__G__em__ep__d__db::Calculate_M17()
{
  M[17][3] = -(Z[113]*Z[207]-Z[211]*Z[205])*Z[128];
  M[17][6] = -(Z[138]*Z[362]-Z[143]*Z[364])*Z[191];
}

void V2_4__G__G__em__ep__d__db::Calculate_M18()
{
  M[18][3] = -Z[128]*Z[155]*Z[126];
  M[18][6] = -Z[191]*Z[68]*Z[357];
}

