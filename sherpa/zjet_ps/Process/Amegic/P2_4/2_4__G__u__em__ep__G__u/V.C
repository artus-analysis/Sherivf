#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__u__em__ep__G__u(Basic_Sfuncs* bs) {
  return new V2_4__G__u__em__ep__G__u(bs);
}

V2_4__G__u__em__ep__G__u::V2_4__G__u__em__ep__G__u(Basic_Sfuncs* _BS) :
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

V2_4__G__u__em__ep__G__u::~V2_4__G__u__em__ep__G__u()
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

Complex V2_4__G__u__em__ep__G__u::Evaluate(int m,int n)
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

void V2_4__G__u__em__ep__G__u::Calculate_M0()
{
  M[0][0] = Z[61]*Z[45]*Z[44];
  M[0][1] = Z[84]*Z[45]*Z[80];
  M[0][2] = -Z[116]*Z[1]*Z[100];
  M[0][3] = Z[135]*Z[131]*Z[130];
  M[0][4] = (Z[142]*Z[141]-Z[139]*Z[138])*Z[145];
  M[0][5] = (Z[142]*Z[175]-Z[139]*Z[154])*Z[188];
  M[0][6] = -(Z[200]*Z[91]+Z[203]*Z[97])*Z[205];
  M[0][7] = (Z[208]*Z[71]-Z[203]*Z[66])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M1()
{
  M[1][1] = Z[84]*Z[45]*Z[221];
  M[1][3] = (Z[227]*Z[130]-Z[225]*Z[121])*Z[135];
  M[1][4] = Z[145]*Z[142]*Z[231];
  M[1][5] = (Z[142]*Z[235]-Z[139]*Z[233])*Z[188];
  M[1][6] = -(Z[241]*Z[91]+Z[242]*Z[97])*Z[205];
  M[1][7] = (Z[243]*Z[71]-Z[242]*Z[66])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M2()
{
  M[2][3] = -Z[135]*Z[127]*Z[256];
  M[2][5] = -Z[188]*Z[139]*Z[163];
}

void V2_4__G__u__em__ep__G__u::Calculate_M3()
{
  M[3][0] = Z[61]*Z[45]*Z[271];
  M[3][2] = -(Z[268]*Z[107]+Z[267]*Z[100])*Z[116];
  M[3][3] = -(Z[226]*Z[256]+Z[225]*Z[255])*Z[135];
  M[3][5] = -Z[188]*Z[139]*Z[234];
}

void V2_4__G__u__em__ep__G__u::Calculate_M12()
{
  M[12][0] = Z[61]*Z[45]*Z[307];
  M[12][1] = Z[84]*Z[45]*Z[325];
  M[12][2] = -Z[116]*Z[1]*Z[332];
  M[12][3] = Z[135]*Z[131]*Z[337];
  M[12][4] = (Z[142]*Z[339]-Z[139]*Z[338])*Z[145];
  M[12][5] = (Z[142]*Z[362]-Z[139]*Z[346])*Z[188];
  M[12][6] = -(Z[197]*Z[328]+Z[203]*Z[331])*Z[205];
  M[12][7] = (Z[211]*Z[323]-Z[203]*Z[320])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M13()
{
  M[13][1] = Z[84]*Z[45]*Z[373];
  M[13][3] = (Z[227]*Z[337]-Z[225]*Z[335])*Z[135];
  M[13][4] = Z[145]*Z[142]*Z[374];
  M[13][5] = (Z[142]*Z[377]-Z[139]*Z[375])*Z[188];
  M[13][6] = -(Z[240]*Z[328]+Z[242]*Z[331])*Z[205];
  M[13][7] = (Z[244]*Z[323]-Z[242]*Z[320])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M14()
{
  M[14][3] = -Z[135]*Z[127]*Z[387];
  M[14][5] = -Z[188]*Z[139]*Z[353];
}

void V2_4__G__u__em__ep__G__u::Calculate_M15()
{
  M[15][0] = Z[61]*Z[45]*Z[391];
  M[15][2] = -(Z[268]*Z[333]+Z[267]*Z[332])*Z[116];
  M[15][3] = -(Z[226]*Z[387]+Z[225]*Z[386])*Z[135];
  M[15][5] = -Z[188]*Z[139]*Z[376];
}

void V2_4__G__u__em__ep__G__u::Calculate_M16()
{
  M[16][0] = (Z[395]*Z[18]+Z[396]*Z[44])*Z[61];
  M[16][1] = (Z[395]*Z[74]+Z[396]*Z[80])*Z[84];
  M[16][2] = -Z[116]*Z[1]*Z[403];
  M[16][3] = Z[135]*Z[131]*Z[430];
  M[16][4] = -Z[145]*Z[433]*Z[138];
  M[16][5] = -Z[188]*Z[433]*Z[154];
  M[16][6] = -(Z[438]*Z[91]+Z[439]*Z[97])*Z[205];
  M[16][7] = (Z[440]*Z[71]-Z[439]*Z[66])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M17()
{
  M[17][1] = (Z[395]*Z[215]+Z[396]*Z[221])*Z[84];
  M[17][3] = (Z[227]*Z[430]-Z[225]*Z[422])*Z[135];
  M[17][5] = -Z[188]*Z[433]*Z[233];
  M[17][6] = -(Z[444]*Z[91]+Z[445]*Z[97])*Z[205];
  M[17][7] = (Z[446]*Z[71]-Z[445]*Z[66])*Z[212];
}

void V2_4__G__u__em__ep__G__u::Calculate_M18()
{
  M[18][3] = -Z[135]*Z[127]*Z[449];
  M[18][5] = (Z[451]*Z[187]-Z[433]*Z[163])*Z[188];
}

void V2_4__G__u__em__ep__G__u::Calculate_M19()
{
  M[19][0] = (Z[395]*Z[269]+Z[396]*Z[271])*Z[61];
  M[19][2] = -(Z[268]*Z[410]+Z[267]*Z[403])*Z[116];
  M[19][3] = -(Z[226]*Z[449]+Z[225]*Z[448])*Z[135];
  M[19][5] = (Z[451]*Z[236]-Z[433]*Z[234])*Z[188];
}

void V2_4__G__u__em__ep__G__u::Calculate_M28()
{
  M[28][0] = (Z[395]*Z[287]+Z[396]*Z[307])*Z[61];
  M[28][1] = (Z[395]*Z[324]+Z[396]*Z[325])*Z[84];
  M[28][2] = -Z[116]*Z[1]*Z[458];
  M[28][3] = Z[135]*Z[131]*Z[463];
  M[28][4] = -Z[145]*Z[433]*Z[338];
  M[28][5] = -Z[188]*Z[433]*Z[346];
  M[28][6] = -(Z[437]*Z[328]+Z[439]*Z[331])*Z[205];
  M[28][7] = (Z[441]*Z[323]-Z[439]*Z[320])*Z[212];
}

