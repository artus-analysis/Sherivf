#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__G__em__ep__G__u__S0_4(Basic_Sfuncs* bs) {
  return new V2_4__u__G__em__ep__G__u__S0_4(bs);
}

V2_4__u__G__em__ep__G__u__S0_4::V2_4__u__G__em__ep__G__u__S0_4(Basic_Sfuncs* _BS) :
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

V2_4__u__G__em__ep__G__u__S0_4::~V2_4__u__G__em__ep__G__u__S0_4()
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

Complex V2_4__u__G__em__ep__G__u__S0_4::Evaluate(int m,int n)
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

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M0()
{
  M[0][0] = Z[61]*Z[45]*Z[44];
  M[0][1] = -Z[93]*Z[13]*Z[88];
  M[0][2] = -Z[113]*Z[45]*Z[109];
  M[0][3] = -(Z[131]*Z[69]+Z[139]*Z[75])*Z[145];
  M[0][4] = -(Z[152]*Z[35]+Z[149]*Z[8]-Z[147]*Z[97])*Z[153];
  M[0][5] = -Z[162]*Z[108]*Z[158];
  M[0][6] = (Z[172]*Z[171]-Z[164]*Z[163])*Z[176];
  M[0][7] = Z[203]*Z[108]*Z[197];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M1()
{
  M[1][0] = Z[61]*Z[45]*Z[207];
  M[1][1] = -Z[93]*Z[204]*Z[88];
  M[1][2] = -Z[113]*Z[45]*Z[211];
  M[1][3] = -(Z[221]*Z[69]+Z[227]*Z[75])*Z[145];
  M[1][4] = -(Z[152]*Z[39]+Z[149]*Z[12]-Z[147]*Z[180])*Z[153];
  M[1][5] = -Z[162]*Z[108]*Z[233];
  M[1][6] = (Z[235]*Z[171]-Z[164]*Z[168])*Z[176];
  M[1][7] = Z[203]*Z[108]*Z[238];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M2()
{
  M[2][0] = Z[61]*Z[45]*Z[244];
  M[2][1] = -Z[93]*Z[240]*Z[77];
  M[2][2] = -Z[113]*Z[45]*Z[254];
  M[2][3] = -(Z[262]*Z[69]+Z[265]*Z[75])*Z[145];
  M[2][4] = -(Z[270]*Z[35]+Z[269]*Z[8]-Z[268]*Z[97])*Z[153];
  M[2][5] = -(Z[253]*Z[158]-Z[252]*Z[155])*Z[162];
  M[2][6] = Z[176]*Z[172]*Z[280];
  M[2][7] = (Z[253]*Z[197]-Z[252]*Z[184])*Z[203];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M3()
{
  M[3][0] = Z[61]*Z[45]*Z[286];
  M[3][1] = -Z[93]*Z[240]*Z[84];
  M[3][2] = -Z[113]*Z[45]*Z[290];
  M[3][3] = -(Z[294]*Z[69]+Z[296]*Z[75])*Z[145];
  M[3][4] = -(Z[270]*Z[39]+Z[269]*Z[12]-Z[268]*Z[180])*Z[153];
  M[3][5] = -(Z[253]*Z[233]-Z[252]*Z[231])*Z[162];
  M[3][6] = (Z[235]*Z[280]-Z[164]*Z[277])*Z[176];
  M[3][7] = (Z[253]*Z[238]-Z[252]*Z[236])*Z[203];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M12()
{
  M[12][0] = Z[61]*Z[45]*Z[327];
  M[12][1] = -Z[93]*Z[13]*Z[346];
  M[12][2] = -Z[113]*Z[45]*Z[355];
  M[12][3] = -(Z[123]*Z[340]+Z[139]*Z[343])*Z[145];
  M[12][4] = -(Z[152]*Z[320]+Z[149]*Z[300]-Z[147]*Z[349])*Z[153];
  M[12][5] = -Z[162]*Z[108]*Z[359];
  M[12][6] = (Z[172]*Z[363]-Z[164]*Z[361])*Z[176];
  M[12][7] = Z[203]*Z[108]*Z[379];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M13()
{
  M[13][0] = Z[61]*Z[45]*Z[386];
  M[13][1] = -Z[93]*Z[204]*Z[346];
  M[13][2] = -Z[113]*Z[45]*Z[390];
  M[13][3] = -(Z[215]*Z[340]+Z[227]*Z[343])*Z[145];
  M[13][4] = -(Z[152]*Z[323]+Z[149]*Z[303]-Z[147]*Z[366])*Z[153];
  M[13][5] = -Z[162]*Z[108]*Z[394];
  M[13][6] = (Z[235]*Z[363]-Z[164]*Z[362])*Z[176];
  M[13][7] = Z[203]*Z[108]*Z[398];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M14()
{
  M[14][0] = Z[61]*Z[45]*Z[402];
  M[14][1] = -Z[93]*Z[240]*Z[344];
  M[14][2] = -Z[113]*Z[45]*Z[406];
  M[14][3] = -(Z[259]*Z[340]+Z[265]*Z[343])*Z[145];
  M[14][4] = -(Z[270]*Z[320]+Z[269]*Z[300]-Z[268]*Z[349])*Z[153];
  M[14][5] = -(Z[253]*Z[359]-Z[252]*Z[357])*Z[162];
  M[14][6] = Z[176]*Z[172]*Z[409];
  M[14][7] = (Z[253]*Z[379]-Z[252]*Z[369])*Z[203];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M15()
{
  M[15][0] = Z[61]*Z[45]*Z[412];
  M[15][1] = -Z[93]*Z[240]*Z[345];
  M[15][2] = -Z[113]*Z[45]*Z[416];
  M[15][3] = -(Z[292]*Z[340]+Z[296]*Z[343])*Z[145];
  M[15][4] = -(Z[270]*Z[323]+Z[269]*Z[303]-Z[268]*Z[366])*Z[153];
  M[15][5] = -(Z[253]*Z[394]-Z[252]*Z[392])*Z[162];
  M[15][6] = (Z[235]*Z[409]-Z[164]*Z[408])*Z[176];
  M[15][7] = (Z[253]*Z[398]-Z[252]*Z[396])*Z[203];
}

void V2_4__u__G__em__ep__G__u__S0_4::Calculate_M16()
{
  M[16][0] = (Z[418]*Z[18]+Z[419]*Z[44])*Z[61];
  M[16][1] = -Z[93]*Z[13]*Z[437];
  M[16][2] = -(Z[418]*Z[104]+Z[419]*Z[109])*Z[113];
  M[16][3] = -(Z[446]*Z[69]+Z[448]*Z[75])*Z[145];
  M[16][4] = -(Z[452]*Z[35]+Z[451]*Z[8]-Z[450]*Z[97])*Z[153];
  M[16][5] = -Z[162]*Z[108]*Z[457];
  M[16][6] = -Z[176]*Z[459]*Z[163];
  M[16][7] = Z[203]*Z[108]*Z[463];
}

