#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__u__ub__em__ep__u__ub__S0_1(Basic_Sfuncs* bs) {
  return new V2_4__u__ub__em__ep__u__ub__S0_1(bs);
}

V2_4__u__ub__em__ep__u__ub__S0_1::V2_4__u__ub__em__ep__u__ub__S0_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[7];
  Z = new Complex[310];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__u__ub__em__ep__u__ub__S0_1::~V2_4__u__ub__em__ep__u__ub__S0_1()
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

Complex V2_4__u__ub__em__ep__u__ub__S0_1::Evaluate(int m,int n)
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
    case 28: Calculate_M28(); break;
    case 29: Calculate_M29(); break;
    case 34: Calculate_M34(); break;
    case 35: Calculate_M35(); break;
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

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M0()
{
  M[0][0] = (Z[25]*Z[21]-Z[16]*Z[12])*Z[32];
  M[0][1] = (Z[40]*Z[36]+Z[46]*Z[42])*Z[49];
  M[0][2] = (Z[56]*Z[52]-Z[60]*Z[42])*Z[63];
  M[0][3] = -(Z[67]*Z[42]+Z[72]*Z[68])*Z[76];
  M[0][4] = -(Z[25]*Z[77]-Z[16]*Z[78])*Z[80];
  M[0][5] = -(Z[82]*Z[40]+Z[83]*Z[46])*Z[85];
  M[0][6] = (Z[83]*Z[67]+Z[86]*Z[72])*Z[88];
  M[0][7] = -(Z[91]*Z[56]-Z[83]*Z[60])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M1()
{
  M[1][0] = (Z[114]*Z[21]-Z[106]*Z[12])*Z[32];
  M[1][1] = (Z[40]*Z[121]+Z[46]*Z[123])*Z[49];
  M[1][2] = (Z[56]*Z[126]-Z[60]*Z[123])*Z[63];
  M[1][3] = -(Z[67]*Z[123]+Z[72]*Z[127])*Z[76];
  M[1][4] = -(Z[114]*Z[77]-Z[106]*Z[78])*Z[80];
  M[1][5] = -(Z[130]*Z[40]+Z[131]*Z[46])*Z[85];
  M[1][6] = (Z[131]*Z[67]+Z[132]*Z[72])*Z[88];
  M[1][7] = -(Z[136]*Z[56]-Z[131]*Z[60])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M2()
{
  M[2][4] = -(Z[11]*Z[150]-Z[20]*Z[78])*Z[80];
  M[2][5] = -(Z[152]*Z[40]+Z[93]*Z[46])*Z[85];
  M[2][6] = (Z[93]*Z[67]+Z[153]*Z[72])*Z[88];
  M[2][7] = -(Z[90]*Z[142]-Z[93]*Z[146])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M3()
{
  M[3][4] = -(Z[102]*Z[150]-Z[110]*Z[78])*Z[80];
  M[3][5] = -(Z[159]*Z[40]+Z[138]*Z[46])*Z[85];
  M[3][6] = (Z[138]*Z[67]+Z[160]*Z[72])*Z[88];
  M[3][7] = -(Z[135]*Z[142]-Z[138]*Z[146])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M12()
{
  M[12][0] = (Z[176]*Z[21]-Z[170]*Z[12])*Z[32];
  M[12][1] = (Z[182]*Z[33]+Z[185]*Z[42])*Z[49];
  M[12][2] = (Z[188]*Z[50]-Z[191]*Z[42])*Z[63];
  M[12][3] = -(Z[194]*Z[42]+Z[197]*Z[73])*Z[76];
  M[12][4] = -(Z[176]*Z[77]-Z[170]*Z[78])*Z[80];
  M[12][5] = -(Z[81]*Z[182]+Z[83]*Z[185])*Z[85];
  M[12][6] = (Z[83]*Z[194]+Z[87]*Z[197])*Z[88];
  M[12][7] = -(Z[89]*Z[188]-Z[83]*Z[191])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M13()
{
  M[13][0] = (Z[212]*Z[21]-Z[206]*Z[12])*Z[32];
  M[13][1] = (Z[182]*Z[119]+Z[185]*Z[123])*Z[49];
  M[13][2] = (Z[188]*Z[125]-Z[191]*Z[123])*Z[63];
  M[13][3] = -(Z[194]*Z[123]+Z[197]*Z[128])*Z[76];
  M[13][4] = -(Z[212]*Z[77]-Z[206]*Z[78])*Z[80];
  M[13][5] = -(Z[129]*Z[182]+Z[131]*Z[185])*Z[85];
  M[13][6] = (Z[131]*Z[194]+Z[133]*Z[197])*Z[88];
  M[13][7] = -(Z[134]*Z[188]-Z[131]*Z[191])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M14()
{
  M[14][4] = -(Z[167]*Z[150]-Z[173]*Z[78])*Z[80];
  M[14][5] = -(Z[151]*Z[182]+Z[93]*Z[185])*Z[85];
  M[14][6] = (Z[93]*Z[194]+Z[154]*Z[197])*Z[88];
  M[14][7] = -(Z[92]*Z[218]-Z[93]*Z[220])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M15()
{
  M[15][4] = -(Z[203]*Z[150]-Z[209]*Z[78])*Z[80];
  M[15][5] = -(Z[158]*Z[182]+Z[138]*Z[185])*Z[85];
  M[15][6] = (Z[138]*Z[194]+Z[161]*Z[197])*Z[88];
  M[15][7] = -(Z[137]*Z[218]-Z[138]*Z[220])*Z[94];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M16()
{
  M[16][0] = (Z[11]*Z[221]+Z[29]*Z[21])*Z[32];
  M[16][1] = (Z[225]*Z[35]+Z[229]*Z[47])*Z[49];
  M[16][2] = (Z[56]*Z[231]-Z[60]*Z[47])*Z[63];
  M[16][3] = -(Z[67]*Z[47]+Z[72]*Z[232])*Z[76];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M17()
{
  M[17][0] = (Z[102]*Z[221]+Z[118]*Z[21])*Z[32];
  M[17][1] = (Z[225]*Z[120]+Z[229]*Z[124])*Z[49];
  M[17][2] = (Z[56]*Z[238]-Z[60]*Z[124])*Z[63];
  M[17][3] = -(Z[67]*Z[124]+Z[72]*Z[239])*Z[76];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M28()
{
  M[28][0] = (Z[167]*Z[221]+Z[179]*Z[21])*Z[32];
  M[28][1] = (Z[258]*Z[41]+Z[260]*Z[47])*Z[49];
  M[28][2] = (Z[188]*Z[230]-Z[191]*Z[47])*Z[63];
  M[28][3] = -(Z[194]*Z[47]+Z[197]*Z[233])*Z[76];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M29()
{
  M[29][0] = (Z[203]*Z[221]+Z[215]*Z[21])*Z[32];
  M[29][1] = (Z[258]*Z[122]+Z[260]*Z[124])*Z[49];
  M[29][2] = (Z[188]*Z[237]-Z[191]*Z[124])*Z[63];
  M[29][3] = -(Z[194]*Z[124]+Z[197]*Z[240])*Z[76];
}

void V2_4__u__ub__em__ep__u__ub__S0_1::Calculate_M34()
{
  M[34][0] = (Z[7]*Z[150]+Z[25]*Z[277])*Z[32];
  M[34][1] = (Z[40]*Z[280]+Z[46]*Z[147])*Z[49];
  M[34][2] = (Z[142]*Z[261]-Z[146]*Z[147])*Z[63];
  M[34][3] = -(Z[265]*Z[147]+Z[270]*Z[149])*Z[76];
}

