#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__db__G__em__ep__G__db__S5_1(Basic_Sfuncs* bs) {
  return new V2_4__db__G__em__ep__G__db__S5_1(bs);
}

V2_4__db__G__em__ep__G__db__S5_1::V2_4__db__G__em__ep__G__db__S5_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[560];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__db__G__em__ep__G__db__S5_1::~V2_4__db__G__em__ep__G__db__S5_1()
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

Complex V2_4__db__G__em__ep__G__db__S5_1::Evaluate(int m,int n)
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

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M0()
{
  M[0][0] = -(Z[19]*Z[18]-Z[46]*Z[45])*Z[62];
  M[0][1] = (Z[19]*Z[74]-Z[46]*Z[79])*Z[82];
  M[0][3] = -(Z[119]*Z[8]+Z[123]*Z[69]-Z[121]*Z[36])*Z[125];
  M[0][4] = -(Z[129]*Z[86]+Z[137]*Z[91])*Z[150];
  M[0][5] = Z[167]*Z[152]*Z[151];
  M[0][6] = (Z[63]*Z[168]+Z[65]*Z[172])*Z[175];
  M[0][7] = -(Z[63]*Z[180]+Z[65]*Z[193])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M1()
{
  M[1][0] = -(Z[19]*Z[204]-Z[46]*Z[206])*Z[62];
  M[1][1] = (Z[19]*Z[208]-Z[46]*Z[210])*Z[82];
  M[1][2] = Z[110]*Z[1]*Z[101];
  M[1][3] = -(Z[119]*Z[12]+Z[123]*Z[189]-Z[121]*Z[40])*Z[125];
  M[1][4] = -(Z[214]*Z[86]+Z[220]*Z[91])*Z[150];
  M[1][5] = Z[167]*Z[152]*Z[159];
  M[1][6] = (Z[63]*Z[231]+Z[65]*Z[233])*Z[175];
  M[1][7] = -(Z[63]*Z[235]+Z[65]*Z[237])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M2()
{
  M[2][0] = -Z[62]*Z[239]*Z[18];
  M[2][1] = Z[82]*Z[239]*Z[74];
  M[2][2] = Z[110]*Z[1]*Z[246];
  M[2][3] = -(Z[261]*Z[8]+Z[263]*Z[69]-Z[262]*Z[36])*Z[125];
  M[2][4] = -(Z[264]*Z[86]+Z[266]*Z[91])*Z[150];
  M[2][5] = Z[167]*Z[271]*Z[162];
  M[2][6] = (Z[63]*Z[272]+Z[65]*Z[276])*Z[175];
  M[2][7] = -(Z[63]*Z[279]+Z[65]*Z[281])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M3()
{
  M[3][0] = -Z[62]*Z[239]*Z[204];
  M[3][1] = Z[82]*Z[239]*Z[208];
  M[3][2] = Z[110]*Z[1]*Z[250];
  M[3][3] = -(Z[261]*Z[12]+Z[263]*Z[189]-Z[262]*Z[40])*Z[125];
  M[3][4] = -(Z[283]*Z[86]+Z[285]*Z[91])*Z[150];
  M[3][5] = Z[167]*Z[289]*Z[162];
  M[3][6] = (Z[63]*Z[290]+Z[65]*Z[292])*Z[175];
  M[3][7] = -(Z[63]*Z[294]+Z[65]*Z[296])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M12()
{
  M[12][0] = -(Z[19]*Z[307]-Z[46]*Z[327])*Z[62];
  M[12][1] = (Z[19]*Z[344]-Z[46]*Z[346])*Z[82];
  M[12][3] = -(Z[119]*Z[300]+Z[123]*Z[340]-Z[121]*Z[320])*Z[125];
  M[12][4] = -(Z[129]*Z[350]+Z[145]*Z[353])*Z[150];
  M[12][5] = Z[167]*Z[152]*Z[356];
  M[12][6] = (Z[63]*Z[359]+Z[65]*Z[361])*Z[175];
  M[12][7] = -(Z[63]*Z[366]+Z[65]*Z[376])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M13()
{
  M[13][0] = -(Z[19]*Z[383]-Z[46]*Z[385])*Z[62];
  M[13][1] = (Z[19]*Z[387]-Z[46]*Z[389])*Z[82];
  M[13][2] = Z[110]*Z[1]*Z[354];
  M[13][3] = -(Z[119]*Z[303]+Z[123]*Z[373]-Z[121]*Z[323])*Z[125];
  M[13][4] = -(Z[214]*Z[350]+Z[226]*Z[353])*Z[150];
  M[13][5] = Z[167]*Z[152]*Z[357];
  M[13][6] = (Z[63]*Z[391]+Z[65]*Z[393])*Z[175];
  M[13][7] = -(Z[63]*Z[395]+Z[65]*Z[397])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M14()
{
  M[14][0] = -Z[62]*Z[239]*Z[307];
  M[14][1] = Z[82]*Z[239]*Z[344];
  M[14][2] = Z[110]*Z[1]*Z[399];
  M[14][3] = -(Z[261]*Z[300]+Z[263]*Z[340]-Z[262]*Z[320])*Z[125];
  M[14][4] = -(Z[264]*Z[350]+Z[268]*Z[353])*Z[150];
  M[14][5] = Z[167]*Z[271]*Z[358];
  M[14][6] = (Z[63]*Z[402]+Z[65]*Z[404])*Z[175];
  M[14][7] = -(Z[63]*Z[406]+Z[65]*Z[408])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M15()
{
  M[15][0] = -Z[62]*Z[239]*Z[383];
  M[15][1] = Z[82]*Z[239]*Z[387];
  M[15][2] = Z[110]*Z[1]*Z[400];
  M[15][3] = -(Z[261]*Z[303]+Z[263]*Z[373]-Z[262]*Z[323])*Z[125];
  M[15][4] = -(Z[283]*Z[350]+Z[287]*Z[353])*Z[150];
  M[15][5] = Z[167]*Z[289]*Z[358];
  M[15][6] = (Z[63]*Z[410]+Z[65]*Z[412])*Z[175];
  M[15][7] = -(Z[63]*Z[414]+Z[65]*Z[416])*Z[202];
}

void V2_4__db__G__em__ep__G__db__S5_1::Calculate_M16()
{
  M[16][0] = -(Z[19]*Z[420]-Z[46]*Z[422])*Z[62];
  M[16][1] = (Z[19]*Z[426]-Z[46]*Z[431])*Z[82];
  M[16][2] = -Z[110]*Z[419]*Z[105];
  M[16][3] = -(Z[437]*Z[8]+Z[439]*Z[69]-Z[438]*Z[36])*Z[125];
  M[16][4] = -(Z[441]*Z[86]+Z[445]*Z[91])*Z[150];
  M[16][5] = Z[167]*Z[152]*Z[452];
  M[16][6] = Z[175]*Z[424]*Z[168];
  M[16][7] = -Z[202]*Z[424]*Z[180];
}

