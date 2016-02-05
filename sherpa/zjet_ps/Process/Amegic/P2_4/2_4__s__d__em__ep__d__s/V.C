#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__s__d__em__ep__d__s(Basic_Sfuncs* bs) {
  return new V2_4__s__d__em__ep__d__s(bs);
}

V2_4__s__d__em__ep__d__s::V2_4__s__d__em__ep__d__s(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[7];
  Z = new Complex[244];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__s__d__em__ep__d__s::~V2_4__s__d__em__ep__d__s()
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

Complex V2_4__s__d__em__ep__d__s::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
    case 32: Calculate_M32(); break;
    case 33: Calculate_M33(); break;
    case 44: Calculate_M44(); break;
    case 45: Calculate_M45(); break;
    case 50: Calculate_M50(); break;
    case 51: Calculate_M51(); break;
    case 62: Calculate_M62(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__s__d__em__ep__d__s::Calculate_M0()
{
  M[0][0] = (Z[10]*Z[9]+Z[15]*Z[14])*Z[18];
  M[0][1] = -(Z[27]*Z[26]-Z[15]*Z[22])*Z[31];
  M[0][2] = (Z[39]*Z[35]+Z[44]*Z[15])*Z[48];
  M[0][3] = (Z[61]*Z[60]+Z[70]*Z[69])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M1()
{
  M[1][0] = (Z[78]*Z[9]+Z[79]*Z[14])*Z[18];
  M[1][1] = -(Z[80]*Z[26]-Z[79]*Z[22])*Z[31];
  M[1][2] = (Z[39]*Z[84]+Z[44]*Z[79])*Z[48];
  M[1][3] = (Z[61]*Z[98]+Z[70]*Z[106])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M12()
{
  M[12][0] = (Z[5]*Z[127]+Z[15]*Z[130])*Z[18];
  M[12][1] = -(Z[29]*Z[136]-Z[15]*Z[133])*Z[31];
  M[12][2] = (Z[139]*Z[32]+Z[142]*Z[15])*Z[48];
  M[12][3] = (Z[61]*Z[151]+Z[70]*Z[157])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M13()
{
  M[13][0] = (Z[77]*Z[127]+Z[79]*Z[130])*Z[18];
  M[13][1] = -(Z[81]*Z[136]-Z[79]*Z[133])*Z[31];
  M[13][2] = (Z[139]*Z[82]+Z[142]*Z[79])*Z[48];
  M[13][3] = (Z[61]*Z[169]+Z[70]*Z[175])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M18()
{
  M[18][0] = (Z[111]*Z[187]+Z[113]*Z[191])*Z[18];
  M[18][1] = -(Z[193]*Z[121]-Z[113]*Z[116])*Z[31];
  M[18][2] = (Z[39]*Z[198]+Z[44]*Z[113])*Z[48];
  M[18][3] = (Z[202]*Z[69]-Z[201]*Z[52])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M19()
{
  M[19][0] = (Z[122]*Z[187]+Z[124]*Z[191])*Z[18];
  M[19][1] = -(Z[195]*Z[121]-Z[124]*Z[116])*Z[31];
  M[19][2] = (Z[39]*Z[205]+Z[44]*Z[124])*Z[48];
  M[19][3] = (Z[202]*Z[106]-Z[201]*Z[90])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M30()
{
  M[30][0] = (Z[112]*Z[210]+Z[113]*Z[212])*Z[18];
  M[30][1] = -(Z[192]*Z[183]-Z[113]*Z[180])*Z[31];
  M[30][2] = (Z[139]*Z[196]+Z[142]*Z[113])*Z[48];
  M[30][3] = (Z[202]*Z[157]-Z[201]*Z[145])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M31()
{
  M[31][0] = (Z[123]*Z[210]+Z[124]*Z[212])*Z[18];
  M[31][1] = -(Z[194]*Z[183]-Z[124]*Z[180])*Z[31];
  M[31][2] = (Z[139]*Z[203]+Z[142]*Z[124])*Z[48];
  M[31][3] = (Z[202]*Z[175]-Z[201]*Z[163])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M32()
{
  M[32][0] = (Z[214]*Z[9]+Z[45]*Z[14])*Z[18];
  M[32][1] = -(Z[215]*Z[26]-Z[45]*Z[22])*Z[31];
  M[32][2] = (Z[220]*Z[34]+Z[224]*Z[45])*Z[48];
  M[32][3] = (Z[70]*Z[74]-Z[225]*Z[56])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M33()
{
  M[33][0] = (Z[227]*Z[9]+Z[86]*Z[14])*Z[18];
  M[33][1] = -(Z[228]*Z[26]-Z[86]*Z[22])*Z[31];
  M[33][2] = (Z[220]*Z[83]+Z[224]*Z[86])*Z[48];
  M[33][3] = (Z[70]*Z[110]-Z[225]*Z[94])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M44()
{
  M[44][0] = (Z[213]*Z[127]+Z[45]*Z[130])*Z[18];
  M[44][1] = -(Z[216]*Z[136]-Z[45]*Z[133])*Z[31];
  M[44][2] = (Z[236]*Z[40]+Z[238]*Z[45])*Z[48];
  M[44][3] = (Z[70]*Z[160]-Z[225]*Z[148])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M45()
{
  M[45][0] = (Z[226]*Z[127]+Z[86]*Z[130])*Z[18];
  M[45][1] = -(Z[229]*Z[136]-Z[86]*Z[133])*Z[31];
  M[45][2] = (Z[236]*Z[85]+Z[238]*Z[86])*Z[48];
  M[45][3] = (Z[70]*Z[178]-Z[225]*Z[166])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M50()
{
  M[50][0] = (Z[230]*Z[187]+Z[200]*Z[191])*Z[18];
  M[50][1] = -(Z[240]*Z[121]-Z[200]*Z[116])*Z[31];
  M[50][2] = (Z[220]*Z[197]+Z[224]*Z[200])*Z[48];
  M[50][3] = (Z[243]*Z[65]+Z[202]*Z[74])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M51()
{
  M[51][0] = (Z[232]*Z[187]+Z[207]*Z[191])*Z[18];
  M[51][1] = -(Z[242]*Z[121]-Z[207]*Z[116])*Z[31];
  M[51][2] = (Z[220]*Z[204]+Z[224]*Z[207])*Z[48];
  M[51][3] = (Z[243]*Z[102]+Z[202]*Z[110])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M62()
{
  M[62][0] = (Z[231]*Z[210]+Z[200]*Z[212])*Z[18];
  M[62][1] = -(Z[239]*Z[183]-Z[200]*Z[180])*Z[31];
  M[62][2] = (Z[236]*Z[199]+Z[238]*Z[200])*Z[48];
  M[62][3] = (Z[243]*Z[154]+Z[202]*Z[160])*Z[76];
}

void V2_4__s__d__em__ep__d__s::Calculate_M63()
{
  M[63][0] = (Z[233]*Z[210]+Z[207]*Z[212])*Z[18];
  M[63][1] = -(Z[241]*Z[183]-Z[207]*Z[180])*Z[31];
  M[63][2] = (Z[236]*Z[206]+Z[238]*Z[207])*Z[48];
  M[63][3] = (Z[243]*Z[172]+Z[202]*Z[178])*Z[76];
}

