#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__ub__em__ep__G__G__S5_0(Basic_Sfuncs* bs) {
  return new V2_4__u__ub__em__ep__G__G__S5_0(bs);
}

V2_4__u__ub__em__ep__G__G__S5_0::V2_4__u__ub__em__ep__G__G__S5_0(Basic_Sfuncs* _BS) :
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

V2_4__u__ub__em__ep__G__G__S5_0::~V2_4__u__ub__em__ep__G__G__S5_0()
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

Complex V2_4__u__ub__em__ep__G__G__S5_0::Evaluate(int m,int n)
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

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M0()
{
  M[0][0] = -(Z[31]*Z[30]-Z[37]*Z[36])*Z[42];
  M[0][1] = (Z[31]*Z[53]-Z[37]*Z[71])*Z[82];
  M[0][2] = (Z[48]*Z[109]-Z[43]*Z[98])*Z[114];
  M[0][3] = -(Z[122]*Z[7]+Z[124]*Z[16]-Z[127]*Z[25])*Z[129];
  M[0][4] = -(Z[141]*Z[89]-Z[149]*Z[95])*Z[154];
  M[0][5] = Z[164]*Z[35]*Z[160];
  M[0][6] = -Z[195]*Z[35]*Z[188];
  M[0][7] = (Z[170]*Z[206]-Z[165]*Z[196])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M1()
{
  M[1][0] = -(Z[31]*Z[210]-Z[37]*Z[212])*Z[42];
  M[1][1] = (Z[31]*Z[215]-Z[37]*Z[217])*Z[82];
  M[1][2] = (Z[214]*Z[109]-Z[43]*Z[105])*Z[114];
  M[1][3] = -(Z[122]*Z[169]+Z[124]*Z[47]-Z[127]*Z[66])*Z[129];
  M[1][4] = -(Z[227]*Z[89]-Z[233]*Z[95])*Z[154];
  M[1][5] = Z[164]*Z[35]*Z[239];
  M[1][6] = -Z[195]*Z[35]*Z[245];
  M[1][7] = (Z[241]*Z[206]-Z[165]*Z[203])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M2()
{
  M[2][0] = -(Z[161]*Z[34]-Z[37]*Z[39])*Z[42];
  M[2][1] = (Z[161]*Z[62]-Z[37]*Z[80])*Z[82];
  M[2][2] = -Z[114]*Z[43]*Z[255];
  M[2][3] = -(Z[259]*Z[11]+Z[261]*Z[20]-Z[127]*Z[29])*Z[129];
  M[2][4] = -(Z[137]*Z[250]-Z[153]*Z[254])*Z[154];
  M[2][5] = -(Z[38]*Z[159]-Z[35]*Z[162])*Z[164];
  M[2][6] = (Z[38]*Z[183]-Z[35]*Z[193])*Z[195];
  M[2][7] = (Z[174]*Z[264]-Z[165]*Z[262])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M3()
{
  M[3][0] = -(Z[161]*Z[211]-Z[37]*Z[213])*Z[42];
  M[3][1] = (Z[161]*Z[216]-Z[37]*Z[218])*Z[82];
  M[3][2] = -Z[114]*Z[43]*Z[256];
  M[3][3] = -(Z[259]*Z[179]+Z[261]*Z[57]-Z[127]*Z[75])*Z[129];
  M[3][4] = -(Z[224]*Z[250]-Z[236]*Z[254])*Z[154];
  M[3][5] = -(Z[38]*Z[238]-Z[35]*Z[240])*Z[164];
  M[3][6] = (Z[38]*Z[244]-Z[35]*Z[246])*Z[195];
  M[3][7] = (Z[242]*Z[264]-Z[165]*Z[263])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M12()
{
  M[12][0] = -(Z[31]*Z[283]-Z[37]*Z[285])*Z[42];
  M[12][1] = (Z[31]*Z[293]-Z[37]*Z[307])*Z[82];
  M[12][2] = (Z[48]*Z[323]-Z[43]*Z[321])*Z[114];
  M[12][3] = -(Z[122]*Z[267]+Z[124]*Z[273]-Z[127]*Z[279])*Z[129];
  M[12][4] = -(Z[133]*Z[317]-Z[149]*Z[320])*Z[154];
  M[12][5] = Z[164]*Z[35]*Z[326];
  M[12][6] = -Z[195]*Z[35]*Z[343];
  M[12][7] = (Z[170]*Z[350]-Z[165]*Z[348])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M13()
{
  M[13][0] = -(Z[31]*Z[351]-Z[37]*Z[353])*Z[42];
  M[13][1] = (Z[31]*Z[355]-Z[37]*Z[357])*Z[82];
  M[13][2] = (Z[214]*Z[323]-Z[43]*Z[322])*Z[114];
  M[13][3] = -(Z[122]*Z[330]+Z[124]*Z[289]-Z[127]*Z[303])*Z[129];
  M[13][4] = -(Z[221]*Z[317]-Z[233]*Z[320])*Z[154];
  M[13][5] = Z[164]*Z[35]*Z[361];
  M[13][6] = -Z[195]*Z[35]*Z[365];
  M[13][7] = (Z[241]*Z[350]-Z[165]*Z[349])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M14()
{
  M[14][0] = -(Z[161]*Z[284]-Z[37]*Z[286])*Z[42];
  M[14][1] = (Z[161]*Z[300]-Z[37]*Z[314])*Z[82];
  M[14][2] = -Z[114]*Z[43]*Z[372];
  M[14][3] = -(Z[259]*Z[270]+Z[261]*Z[276]-Z[127]*Z[282])*Z[129];
  M[14][4] = -(Z[145]*Z[369]-Z[153]*Z[371])*Z[154];
  M[14][5] = -(Z[38]*Z[325]-Z[35]*Z[327])*Z[164];
  M[14][6] = (Z[38]*Z[339]-Z[35]*Z[347])*Z[195];
  M[14][7] = (Z[174]*Z[377]-Z[165]*Z[375])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M15()
{
  M[15][0] = -(Z[161]*Z[352]-Z[37]*Z[354])*Z[42];
  M[15][1] = (Z[161]*Z[356]-Z[37]*Z[358])*Z[82];
  M[15][2] = -Z[114]*Z[43]*Z[373];
  M[15][3] = -(Z[259]*Z[336]+Z[261]*Z[296]-Z[127]*Z[310])*Z[129];
  M[15][4] = -(Z[230]*Z[369]-Z[236]*Z[371])*Z[154];
  M[15][5] = -(Z[38]*Z[360]-Z[35]*Z[362])*Z[164];
  M[15][6] = (Z[38]*Z[364]-Z[35]*Z[366])*Z[195];
  M[15][7] = (Z[242]*Z[377]-Z[165]*Z[376])*Z[209];
}

void V2_4__u__ub__em__ep__G__G__S5_0::Calculate_M16()
{
  M[16][0] = -(Z[31]*Z[381]-Z[37]*Z[386])*Z[42];
  M[16][1] = (Z[31]*Z[390]-Z[37]*Z[392])*Z[82];
  M[16][2] = -Z[114]*Z[388]*Z[98];
  M[16][3] = -(Z[397]*Z[7]+Z[398]*Z[16]-Z[399]*Z[25])*Z[129];
  M[16][4] = -(Z[405]*Z[89]-Z[409]*Z[95])*Z[154];
  M[16][5] = -(Z[384]*Z[157]-Z[385]*Z[160])*Z[164];
  M[16][6] = (Z[384]*Z[175]-Z[385]*Z[188])*Z[195];
  M[16][7] = (Z[170]*Z[422]-Z[165]*Z[412])*Z[209];
}

