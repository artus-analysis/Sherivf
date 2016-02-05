#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__G__ub__em__ep__G__ub__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__G__ub__em__ep__G__ub__S4_1(bs);
}

V2_4__G__ub__em__ep__G__ub__S4_1::V2_4__G__ub__em__ep__G__ub__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[534];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__G__ub__em__ep__G__ub__S4_1::~V2_4__G__ub__em__ep__G__ub__S4_1()
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

Complex V2_4__G__ub__em__ep__G__ub__S4_1::Evaluate(int m,int n)
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

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M0()
{
  M[0][0] = (Z[24]*Z[19]-Z[32]*Z[28])*Z[35];
  M[0][1] = -(Z[32]*Z[39]+Z[47]*Z[43])*Z[54];
  M[0][2] = -(Z[71]*Z[70]-Z[98]*Z[97])*Z[114];
  M[0][3] = -Z[125]*Z[71]*Z[118];
  M[0][4] = -(Z[65]*Z[140]-Z[55]*Z[132])*Z[144];
  M[0][6] = -(Z[161]*Z[160]+Z[165]*Z[164])*Z[168];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M1()
{
  M[1][0] = (Z[214]*Z[19]-Z[216]*Z[28])*Z[35];
  M[1][1] = -(Z[216]*Z[39]+Z[218]*Z[43])*Z[54];
  M[1][2] = -(Z[71]*Z[223]-Z[98]*Z[225])*Z[114];
  M[1][3] = -(Z[71]*Z[230]-Z[98]*Z[234])*Z[125];
  M[1][4] = -Z[144]*Z[222]*Z[140];
  M[1][5] = Z[159]*Z[235]*Z[149];
  M[1][6] = -(Z[161]*Z[237]+Z[165]*Z[241])*Z[168];
  M[1][7] = -(Z[161]*Z[242]+Z[165]*Z[244])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M2()
{
  M[2][2] = -(Z[263]*Z[84]-Z[98]*Z[111])*Z[114];
  M[2][4] = (Z[60]*Z[265]+Z[55]*Z[264])*Z[144];
  M[2][5] = (Z[268]*Z[154]+Z[267]*Z[149])*Z[159];
  M[2][7] = -(Z[161]*Z[271]+Z[165]*Z[273])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M3()
{
  M[3][2] = -(Z[263]*Z[224]-Z[98]*Z[226])*Z[114];
  M[3][4] = Z[144]*Z[221]*Z[265];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M12()
{
  M[12][0] = (Z[15]*Z[282]-Z[32]*Z[285])*Z[35];
  M[12][1] = -(Z[32]*Z[288]+Z[52]*Z[291])*Z[54];
  M[12][2] = -(Z[71]*Z[301]-Z[98]*Z[321])*Z[114];
  M[12][3] = -Z[125]*Z[71]*Z[332];
  M[12][4] = -(Z[65]*Z[335]-Z[55]*Z[333])*Z[144];
  M[12][6] = -(Z[161]*Z[339]+Z[165]*Z[340])*Z[168];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M13()
{
  M[13][0] = (Z[212]*Z[282]-Z[216]*Z[285])*Z[35];
  M[13][1] = -(Z[216]*Z[288]+Z[220]*Z[291])*Z[54];
  M[13][2] = -(Z[71]*Z[369]-Z[98]*Z[371])*Z[114];
  M[13][3] = -(Z[71]*Z[373]-Z[98]*Z[374])*Z[125];
  M[13][4] = -Z[144]*Z[222]*Z[335];
  M[13][5] = Z[159]*Z[235]*Z[336];
  M[13][6] = -(Z[161]*Z[375]+Z[165]*Z[376])*Z[168];
  M[13][7] = -(Z[161]*Z[377]+Z[165]*Z[379])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M14()
{
  M[14][2] = -(Z[263]*Z[311]-Z[98]*Z[331])*Z[114];
  M[14][4] = (Z[60]*Z[387]+Z[55]*Z[386])*Z[144];
  M[14][5] = (Z[268]*Z[337]+Z[267]*Z[336])*Z[159];
  M[14][7] = -(Z[161]*Z[391]+Z[165]*Z[393])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M15()
{
  M[15][2] = -(Z[263]*Z[370]-Z[98]*Z[372])*Z[114];
  M[15][4] = Z[144]*Z[221]*Z[387];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M16()
{
  M[16][0] = (Z[403]*Z[19]-Z[405]*Z[28])*Z[35];
  M[16][1] = -(Z[405]*Z[39]+Z[407]*Z[43])*Z[54];
  M[16][2] = -(Z[410]*Z[70]-Z[411]*Z[97])*Z[114];
  M[16][3] = -Z[125]*Z[410]*Z[118];
  M[16][4] = -(Z[65]*Z[426]-Z[55]*Z[418])*Z[144];
  M[16][6] = -(Z[443]*Z[160]+Z[444]*Z[164])*Z[168];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M17()
{
  M[17][0] = (Z[447]*Z[19]-Z[448]*Z[28])*Z[35];
  M[17][1] = -(Z[448]*Z[39]+Z[449]*Z[43])*Z[54];
  M[17][2] = -(Z[410]*Z[223]-Z[411]*Z[225])*Z[114];
  M[17][3] = -(Z[410]*Z[230]-Z[411]*Z[234])*Z[125];
  M[17][4] = -Z[144]*Z[222]*Z[426];
  M[17][5] = Z[159]*Z[235]*Z[434];
  M[17][6] = -(Z[443]*Z[237]+Z[444]*Z[241])*Z[168];
  M[17][7] = -(Z[443]*Z[242]+Z[444]*Z[244])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M18()
{
  M[18][2] = -(Z[454]*Z[84]-Z[411]*Z[111])*Z[114];
  M[18][4] = (Z[60]*Z[456]+Z[55]*Z[455])*Z[144];
  M[18][5] = (Z[268]*Z[439]+Z[267]*Z[434])*Z[159];
  M[18][7] = -(Z[443]*Z[271]+Z[444]*Z[273])*Z[207];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M19()
{
  M[19][2] = -(Z[454]*Z[224]-Z[411]*Z[226])*Z[114];
  M[19][4] = Z[144]*Z[221]*Z[456];
}

void V2_4__G__ub__em__ep__G__ub__S4_1::Calculate_M28()
{
  M[28][0] = (Z[401]*Z[282]-Z[405]*Z[285])*Z[35];
  M[28][1] = -(Z[405]*Z[288]+Z[409]*Z[291])*Z[54];
  M[28][2] = -(Z[410]*Z[301]-Z[411]*Z[321])*Z[114];
  M[28][3] = -Z[125]*Z[410]*Z[332];
  M[28][4] = -(Z[65]*Z[463]-Z[55]*Z[461])*Z[144];
  M[28][6] = -(Z[443]*Z[339]+Z[444]*Z[340])*Z[168];
}

