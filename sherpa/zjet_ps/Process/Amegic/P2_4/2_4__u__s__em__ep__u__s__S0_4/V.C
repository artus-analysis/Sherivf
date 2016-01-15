#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__s__em__ep__u__s__S0_4(Basic_Sfuncs* bs) {
  return new V2_4__u__s__em__ep__u__s__S0_4(bs);
}

V2_4__u__s__em__ep__u__s__S0_4::V2_4__u__s__em__ep__u__s__S0_4(Basic_Sfuncs* _BS) :
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

V2_4__u__s__em__ep__u__s__S0_4::~V2_4__u__s__em__ep__u__s__S0_4()
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

Complex V2_4__u__s__em__ep__u__s__S0_4::Evaluate(int m,int n)
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

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M0()
{
  M[0][0] = -(Z[10]*Z[9]+Z[15]*Z[14])*Z[18];
  M[0][1] = (Z[27]*Z[26]-Z[15]*Z[22])*Z[31];
  M[0][2] = -(Z[39]*Z[35]+Z[44]*Z[15])*Z[48];
  M[0][3] = -(Z[61]*Z[60]+Z[70]*Z[69])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M1()
{
  M[1][0] = -(Z[78]*Z[9]+Z[79]*Z[14])*Z[18];
  M[1][1] = (Z[80]*Z[26]-Z[79]*Z[22])*Z[31];
  M[1][2] = -(Z[39]*Z[84]+Z[44]*Z[79])*Z[48];
  M[1][3] = -(Z[61]*Z[98]+Z[70]*Z[106])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M12()
{
  M[12][0] = -(Z[5]*Z[127]+Z[15]*Z[130])*Z[18];
  M[12][1] = (Z[29]*Z[136]-Z[15]*Z[133])*Z[31];
  M[12][2] = -(Z[139]*Z[32]+Z[142]*Z[15])*Z[48];
  M[12][3] = -(Z[61]*Z[151]+Z[70]*Z[157])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M13()
{
  M[13][0] = -(Z[77]*Z[127]+Z[79]*Z[130])*Z[18];
  M[13][1] = (Z[81]*Z[136]-Z[79]*Z[133])*Z[31];
  M[13][2] = -(Z[139]*Z[82]+Z[142]*Z[79])*Z[48];
  M[13][3] = -(Z[61]*Z[169]+Z[70]*Z[175])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M16()
{
  M[16][0] = -(Z[185]*Z[9]+Z[45]*Z[14])*Z[18];
  M[16][1] = (Z[186]*Z[26]-Z[45]*Z[22])*Z[31];
  M[16][2] = -(Z[191]*Z[34]+Z[195]*Z[45])*Z[48];
  M[16][3] = -(Z[70]*Z[74]-Z[196]*Z[56])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M17()
{
  M[17][0] = -(Z[198]*Z[9]+Z[86]*Z[14])*Z[18];
  M[17][1] = (Z[199]*Z[26]-Z[86]*Z[22])*Z[31];
  M[17][2] = -(Z[191]*Z[83]+Z[195]*Z[86])*Z[48];
  M[17][3] = -(Z[70]*Z[110]-Z[196]*Z[94])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M28()
{
  M[28][0] = -(Z[184]*Z[127]+Z[45]*Z[130])*Z[18];
  M[28][1] = (Z[187]*Z[136]-Z[45]*Z[133])*Z[31];
  M[28][2] = -(Z[209]*Z[40]+Z[211]*Z[45])*Z[48];
  M[28][3] = -(Z[70]*Z[160]-Z[196]*Z[148])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M29()
{
  M[29][0] = -(Z[197]*Z[127]+Z[86]*Z[130])*Z[18];
  M[29][1] = (Z[200]*Z[136]-Z[86]*Z[133])*Z[31];
  M[29][2] = -(Z[209]*Z[85]+Z[211]*Z[86])*Z[48];
  M[29][3] = -(Z[70]*Z[178]-Z[196]*Z[166])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M34()
{
  M[34][0] = -(Z[111]*Z[215]+Z[113]*Z[219])*Z[18];
  M[34][1] = (Z[221]*Z[121]-Z[113]*Z[116])*Z[31];
  M[34][2] = -(Z[39]*Z[226]+Z[44]*Z[113])*Z[48];
  M[34][3] = -(Z[229]*Z[69]-Z[228]*Z[52])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M35()
{
  M[35][0] = -(Z[122]*Z[215]+Z[124]*Z[219])*Z[18];
  M[35][1] = (Z[223]*Z[121]-Z[124]*Z[116])*Z[31];
  M[35][2] = -(Z[39]*Z[232]+Z[44]*Z[124])*Z[48];
  M[35][3] = -(Z[229]*Z[106]-Z[228]*Z[90])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M46()
{
  M[46][0] = -(Z[112]*Z[236]+Z[113]*Z[238])*Z[18];
  M[46][1] = (Z[220]*Z[183]-Z[113]*Z[180])*Z[31];
  M[46][2] = -(Z[139]*Z[224]+Z[142]*Z[113])*Z[48];
  M[46][3] = -(Z[229]*Z[157]-Z[228]*Z[145])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M47()
{
  M[47][0] = -(Z[123]*Z[236]+Z[124]*Z[238])*Z[18];
  M[47][1] = (Z[222]*Z[183]-Z[124]*Z[180])*Z[31];
  M[47][2] = -(Z[139]*Z[230]+Z[142]*Z[124])*Z[48];
  M[47][3] = -(Z[229]*Z[175]-Z[228]*Z[163])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M50()
{
  M[50][0] = -(Z[201]*Z[215]+Z[203]*Z[219])*Z[18];
  M[50][1] = (Z[240]*Z[121]-Z[203]*Z[116])*Z[31];
  M[50][2] = -(Z[191]*Z[225]+Z[195]*Z[203])*Z[48];
  M[50][3] = -(Z[243]*Z[65]+Z[229]*Z[74])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M51()
{
  M[51][0] = -(Z[204]*Z[215]+Z[206]*Z[219])*Z[18];
  M[51][1] = (Z[242]*Z[121]-Z[206]*Z[116])*Z[31];
  M[51][2] = -(Z[191]*Z[231]+Z[195]*Z[206])*Z[48];
  M[51][3] = -(Z[243]*Z[102]+Z[229]*Z[110])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M62()
{
  M[62][0] = -(Z[202]*Z[236]+Z[203]*Z[238])*Z[18];
  M[62][1] = (Z[239]*Z[183]-Z[203]*Z[180])*Z[31];
  M[62][2] = -(Z[209]*Z[227]+Z[211]*Z[203])*Z[48];
  M[62][3] = -(Z[243]*Z[154]+Z[229]*Z[160])*Z[76];
}

void V2_4__u__s__em__ep__u__s__S0_4::Calculate_M63()
{
  M[63][0] = -(Z[205]*Z[236]+Z[206]*Z[238])*Z[18];
  M[63][1] = (Z[241]*Z[183]-Z[206]*Z[180])*Z[31];
  M[63][2] = -(Z[209]*Z[233]+Z[211]*Z[206])*Z[48];
  M[63][3] = -(Z[243]*Z[172]+Z[229]*Z[178])*Z[76];
}

