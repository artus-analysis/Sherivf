#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__d__ub__em__ep__d__ub__S4_1(Basic_Sfuncs* bs) {
  return new V2_4__d__ub__em__ep__d__ub__S4_1(bs);
}

V2_4__d__ub__em__ep__d__ub__S4_1::V2_4__d__ub__em__ep__d__ub__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[10];
  Z = new Complex[244];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__d__ub__em__ep__d__ub__S4_1::~V2_4__d__ub__em__ep__d__ub__S4_1()
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

Complex V2_4__d__ub__em__ep__d__ub__S4_1::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 16: Calculate_M16(); break;
    case 17: Calculate_M17(); break;
    case 28: Calculate_M28(); break;
    case 29: Calculate_M29(); break;
    case 34: Calculate_M34(); break;
    case 35: Calculate_M35(); break;
    case 46: Calculate_M46(); break;
    case 47: Calculate_M47(); break;
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M0()
{
  M[0][0] = (Z[25]*Z[21]-Z[16]*Z[12])*Z[32];
  M[0][1] = (Z[40]*Z[36]+Z[46]*Z[42])*Z[49];
  M[0][2] = (Z[56]*Z[52]-Z[60]*Z[42])*Z[63];
  M[0][3] = -(Z[67]*Z[42]+Z[72]*Z[68])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M1()
{
  M[1][0] = (Z[96]*Z[21]-Z[88]*Z[12])*Z[32];
  M[1][1] = (Z[40]*Z[103]+Z[46]*Z[105])*Z[49];
  M[1][2] = (Z[56]*Z[108]-Z[60]*Z[105])*Z[63];
  M[1][3] = -(Z[67]*Z[105]+Z[72]*Z[109])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M12()
{
  M[12][0] = (Z[139]*Z[21]-Z[133]*Z[12])*Z[32];
  M[12][1] = (Z[145]*Z[33]+Z[148]*Z[42])*Z[49];
  M[12][2] = (Z[151]*Z[50]-Z[154]*Z[42])*Z[63];
  M[12][3] = -(Z[157]*Z[42]+Z[160]*Z[73])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M13()
{
  M[13][0] = (Z[175]*Z[21]-Z[169]*Z[12])*Z[32];
  M[13][1] = (Z[145]*Z[101]+Z[148]*Z[105])*Z[49];
  M[13][2] = (Z[151]*Z[107]-Z[154]*Z[105])*Z[63];
  M[13][3] = -(Z[157]*Z[105]+Z[160]*Z[110])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M16()
{
  M[16][0] = (Z[11]*Z[184]+Z[29]*Z[21])*Z[32];
  M[16][1] = (Z[188]*Z[35]+Z[192]*Z[47])*Z[49];
  M[16][2] = (Z[56]*Z[194]-Z[60]*Z[47])*Z[63];
  M[16][3] = -(Z[67]*Z[47]+Z[72]*Z[195])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M17()
{
  M[17][0] = (Z[84]*Z[184]+Z[100]*Z[21])*Z[32];
  M[17][1] = (Z[188]*Z[102]+Z[192]*Z[106])*Z[49];
  M[17][2] = (Z[56]*Z[198]-Z[60]*Z[106])*Z[63];
  M[17][3] = -(Z[67]*Z[106]+Z[72]*Z[199])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M28()
{
  M[28][0] = (Z[130]*Z[184]+Z[142]*Z[21])*Z[32];
  M[28][1] = (Z[209]*Z[41]+Z[211]*Z[47])*Z[49];
  M[28][2] = (Z[151]*Z[193]-Z[154]*Z[47])*Z[63];
  M[28][3] = -(Z[157]*Z[47]+Z[160]*Z[196])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M29()
{
  M[29][0] = (Z[166]*Z[184]+Z[178]*Z[21])*Z[32];
  M[29][1] = (Z[209]*Z[104]+Z[211]*Z[106])*Z[49];
  M[29][2] = (Z[151]*Z[197]-Z[154]*Z[106])*Z[63];
  M[29][3] = -(Z[157]*Z[106]+Z[160]*Z[200])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M34()
{
  M[34][0] = (Z[7]*Z[224]+Z[25]*Z[225])*Z[32];
  M[34][1] = (Z[40]*Z[228]+Z[46]*Z[119])*Z[49];
  M[34][2] = (Z[114]*Z[212]-Z[118]*Z[119])*Z[63];
  M[34][3] = -(Z[216]*Z[119]+Z[221]*Z[121])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M35()
{
  M[35][0] = (Z[80]*Z[224]+Z[96]*Z[225])*Z[32];
  M[35][1] = (Z[40]*Z[232]+Z[46]*Z[122])*Z[49];
  M[35][2] = (Z[114]*Z[222]-Z[118]*Z[122])*Z[63];
  M[35][3] = -(Z[216]*Z[122]+Z[221]*Z[124])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M46()
{
  M[46][0] = (Z[127]*Z[224]+Z[139]*Z[225])*Z[32];
  M[46][1] = (Z[145]*Z[226]+Z[148]*Z[119])*Z[49];
  M[46][2] = (Z[181]*Z[213]-Z[183]*Z[119])*Z[63];
  M[46][3] = -(Z[235]*Z[119]+Z[238]*Z[120])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M47()
{
  M[47][0] = (Z[163]*Z[224]+Z[175]*Z[225])*Z[32];
  M[47][1] = (Z[145]*Z[230]+Z[148]*Z[122])*Z[49];
  M[47][2] = (Z[181]*Z[223]-Z[183]*Z[122])*Z[63];
  M[47][3] = -(Z[235]*Z[122]+Z[238]*Z[123])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M50()
{
  M[50][0] = (Z[29]*Z[225]-Z[20]*Z[243])*Z[32];
  M[50][1] = (Z[188]*Z[227]+Z[192]*Z[201])*Z[49];
  M[50][2] = (Z[114]*Z[239]-Z[118]*Z[201])*Z[63];
  M[50][3] = -(Z[216]*Z[201]+Z[221]*Z[203])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M51()
{
  M[51][0] = (Z[100]*Z[225]-Z[92]*Z[243])*Z[32];
  M[51][1] = (Z[188]*Z[231]+Z[192]*Z[204])*Z[49];
  M[51][2] = (Z[114]*Z[241]-Z[118]*Z[204])*Z[63];
  M[51][3] = -(Z[216]*Z[204]+Z[221]*Z[206])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M62()
{
  M[62][0] = (Z[142]*Z[225]-Z[136]*Z[243])*Z[32];
  M[62][1] = (Z[209]*Z[229]+Z[211]*Z[201])*Z[49];
  M[62][2] = (Z[181]*Z[240]-Z[183]*Z[201])*Z[63];
  M[62][3] = -(Z[235]*Z[201]+Z[238]*Z[202])*Z[76];
}

void V2_4__d__ub__em__ep__d__ub__S4_1::Calculate_M63()
{
  M[63][0] = (Z[178]*Z[225]-Z[172]*Z[243])*Z[32];
  M[63][1] = (Z[209]*Z[233]+Z[211]*Z[204])*Z[49];
  M[63][2] = (Z[181]*Z[242]-Z[183]*Z[204])*Z[63];
  M[63][3] = -(Z[235]*Z[204]+Z[238]*Z[205])*Z[76];
}

