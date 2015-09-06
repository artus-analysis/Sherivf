#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_4_16_10_570_64_18_2(Basic_Sfuncs* bs) {
  return new VP2_4_16_10_570_64_18_2(bs);
}

VP2_4_16_10_570_64_18_2::VP2_4_16_10_570_64_18_2(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[570];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

VP2_4_16_10_570_64_18_2::~VP2_4_16_10_570_64_18_2()
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

Complex VP2_4_16_10_570_64_18_2::Evaluate(int m,int n)
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

void VP2_4_16_10_570_64_18_2::Calculate_M0()
{
  M[0][0] = Z[41]*Z[36]*Z[35];
  M[0][1] = -Z[81]*Z[36]*Z[70];
  M[0][2] = (Z[47]*Z[108]-Z[42]*Z[97])*Z[113];
  M[0][3] = -(Z[121]*Z[7]+Z[123]*Z[16]-Z[126]*Z[25])*Z[128];
  M[0][4] = -(Z[140]*Z[88]-Z[148]*Z[94])*Z[153];
  M[0][5] = Z[162]*Z[34]*Z[158];
  M[0][6] = -Z[192]*Z[34]*Z[185];
  M[0][7] = (Z[168]*Z[203]-Z[163]*Z[193])*Z[206];
}

void VP2_4_16_10_570_64_18_2::Calculate_M1()
{
  M[1][0] = Z[41]*Z[36]*Z[209];
  M[1][1] = -Z[81]*Z[36]*Z[214];
  M[1][2] = (Z[211]*Z[108]-Z[42]*Z[104])*Z[113];
  M[1][3] = -(Z[121]*Z[167]+Z[123]*Z[46]-Z[126]*Z[65])*Z[128];
  M[1][4] = -(Z[224]*Z[88]-Z[230]*Z[94])*Z[153];
  M[1][5] = Z[162]*Z[34]*Z[236];
  M[1][6] = -Z[192]*Z[34]*Z[241];
  M[1][7] = (Z[238]*Z[203]-Z[163]*Z[200])*Z[206];
}

void VP2_4_16_10_570_64_18_2::Calculate_M2()
{
  M[2][0] = -(Z[159]*Z[33]-Z[36]*Z[38])*Z[41];
  M[2][1] = (Z[159]*Z[61]-Z[36]*Z[79])*Z[81];
  M[2][2] = -Z[113]*Z[42]*Z[251];
  M[2][3] = -(Z[255]*Z[11]+Z[257]*Z[20]-Z[126]*Z[29])*Z[128];
  M[2][4] = -(Z[136]*Z[246]-Z[152]*Z[250])*Z[153];
  M[2][5] = -(Z[37]*Z[157]-Z[34]*Z[160])*Z[162];
  M[2][6] = (Z[37]*Z[180]-Z[34]*Z[190])*Z[192];
  M[2][7] = -Z[206]*Z[163]*Z[258];
}

void VP2_4_16_10_570_64_18_2::Calculate_M3()
{
  M[3][0] = -(Z[159]*Z[208]-Z[36]*Z[210])*Z[41];
  M[3][1] = (Z[159]*Z[213]-Z[36]*Z[215])*Z[81];
  M[3][2] = -Z[113]*Z[42]*Z[252];
  M[3][3] = -(Z[255]*Z[176]+Z[257]*Z[56]-Z[126]*Z[74])*Z[128];
  M[3][4] = -(Z[221]*Z[246]-Z[233]*Z[250])*Z[153];
  M[3][5] = -(Z[37]*Z[235]-Z[34]*Z[237])*Z[162];
  M[3][6] = (Z[37]*Z[240]-Z[34]*Z[242])*Z[192];
  M[3][7] = -Z[206]*Z[163]*Z[259];
}

void VP2_4_16_10_570_64_18_2::Calculate_M12()
{
  M[12][0] = Z[41]*Z[36]*Z[281];
  M[12][1] = -Z[81]*Z[36]*Z[303];
  M[12][2] = (Z[47]*Z[319]-Z[42]*Z[317])*Z[113];
  M[12][3] = -(Z[121]*Z[263]+Z[123]*Z[269]-Z[126]*Z[275])*Z[128];
  M[12][4] = -(Z[132]*Z[313]-Z[148]*Z[316])*Z[153];
  M[12][5] = Z[162]*Z[34]*Z[322];
  M[12][6] = -Z[192]*Z[34]*Z[339];
  M[12][7] = (Z[168]*Z[346]-Z[163]*Z[344])*Z[206];
}

void VP2_4_16_10_570_64_18_2::Calculate_M13()
{
  M[13][0] = Z[41]*Z[36]*Z[349];
  M[13][1] = -Z[81]*Z[36]*Z[353];
  M[13][2] = (Z[211]*Z[319]-Z[42]*Z[318])*Z[113];
  M[13][3] = -(Z[121]*Z[326]+Z[123]*Z[285]-Z[126]*Z[299])*Z[128];
  M[13][4] = -(Z[218]*Z[313]-Z[230]*Z[316])*Z[153];
  M[13][5] = Z[162]*Z[34]*Z[357];
  M[13][6] = -Z[192]*Z[34]*Z[361];
  M[13][7] = (Z[238]*Z[346]-Z[163]*Z[345])*Z[206];
}

void VP2_4_16_10_570_64_18_2::Calculate_M14()
{
  M[14][0] = -(Z[159]*Z[280]-Z[36]*Z[282])*Z[41];
  M[14][1] = (Z[159]*Z[296]-Z[36]*Z[310])*Z[81];
  M[14][2] = -Z[113]*Z[42]*Z[368];
  M[14][3] = -(Z[255]*Z[266]+Z[257]*Z[272]-Z[126]*Z[278])*Z[128];
  M[14][4] = -(Z[144]*Z[365]-Z[152]*Z[367])*Z[153];
  M[14][5] = -(Z[37]*Z[321]-Z[34]*Z[323])*Z[162];
  M[14][6] = (Z[37]*Z[335]-Z[34]*Z[343])*Z[192];
  M[14][7] = -Z[206]*Z[163]*Z[371];
}

void VP2_4_16_10_570_64_18_2::Calculate_M15()
{
  M[15][0] = -(Z[159]*Z[348]-Z[36]*Z[350])*Z[41];
  M[15][1] = (Z[159]*Z[352]-Z[36]*Z[354])*Z[81];
  M[15][2] = -Z[113]*Z[42]*Z[369];
  M[15][3] = -(Z[255]*Z[332]+Z[257]*Z[292]-Z[126]*Z[306])*Z[128];
  M[15][4] = -(Z[227]*Z[365]-Z[233]*Z[367])*Z[153];
  M[15][5] = -(Z[37]*Z[356]-Z[34]*Z[358])*Z[162];
  M[15][6] = (Z[37]*Z[360]-Z[34]*Z[362])*Z[192];
  M[15][7] = -Z[206]*Z[163]*Z[372];
}

void VP2_4_16_10_570_64_18_2::Calculate_M16()
{
  M[16][0] = Z[41]*Z[36]*Z[382];
  M[16][1] = -Z[81]*Z[36]*Z[388];
  M[16][2] = -Z[113]*Z[384]*Z[97];
  M[16][3] = -(Z[393]*Z[7]+Z[394]*Z[16]-Z[395]*Z[25])*Z[128];
  M[16][4] = -(Z[401]*Z[88]-Z[405]*Z[94])*Z[153];
  M[16][5] = -(Z[380]*Z[155]-Z[381]*Z[158])*Z[162];
  M[16][6] = (Z[380]*Z[172]-Z[381]*Z[185])*Z[192];
  M[16][7] = (Z[168]*Z[418]-Z[163]*Z[408])*Z[206];
}

