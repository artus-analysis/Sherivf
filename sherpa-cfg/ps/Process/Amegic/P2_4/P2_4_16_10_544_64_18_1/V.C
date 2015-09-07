#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_4_16_10_544_64_18_1(Basic_Sfuncs* bs) {
  return new VP2_4_16_10_544_64_18_1(bs);
}

VP2_4_16_10_544_64_18_1::VP2_4_16_10_544_64_18_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Vfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[10];
  Z = new Complex[544];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

VP2_4_16_10_544_64_18_1::~VP2_4_16_10_544_64_18_1()
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

Complex VP2_4_16_10_544_64_18_1::Evaluate(int m,int n)
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

void VP2_4_16_10_544_64_18_1::Calculate_M0()
{
  M[0][0] = (Z[20]*Z[15]+Z[29]*Z[24])*Z[32];
  M[0][1] = -(Z[29]*Z[36]+Z[45]*Z[40])*Z[53];
  M[0][2] = -(Z[71]*Z[70]-Z[61]*Z[60])*Z[76];
  M[0][3] = -(Z[117]*Z[116]-Z[90]*Z[89])*Z[132];
  M[0][4] = -Z[140]*Z[117]*Z[136];
  M[0][5] = -(Z[142]*Z[141]-Z[147]*Z[146])*Z[149];
  M[0][6] = -(Z[142]*Z[160]-Z[147]*Z[181])*Z[195];
  M[0][7] = -Z[209]*Z[159]*Z[206];
}

void VP2_4_16_10_544_64_18_1::Calculate_M1()
{
  M[1][0] = (Z[214]*Z[15]+Z[216]*Z[24])*Z[32];
  M[1][1] = -(Z[216]*Z[36]+Z[218]*Z[40])*Z[53];
  M[1][2] = -Z[76]*Z[222]*Z[70];
  M[1][3] = -(Z[117]*Z[225]-Z[90]*Z[223])*Z[132];
  M[1][4] = -(Z[117]*Z[231]-Z[90]*Z[230])*Z[140];
  M[1][5] = -Z[149]*Z[142]*Z[235];
  M[1][6] = -(Z[142]*Z[242]-Z[147]*Z[244])*Z[195];
  M[1][7] = -(Z[241]*Z[206]-Z[239]*Z[200])*Z[209];
}

void VP2_4_16_10_544_64_18_1::Calculate_M2()
{
  M[2][0] = (Z[252]*Z[15]+Z[254]*Z[24])*Z[32];
  M[2][1] = -(Z[254]*Z[36]+Z[256]*Z[40])*Z[53];
  M[2][2] = -(Z[71]*Z[273]-Z[61]*Z[265])*Z[76];
  M[2][3] = -(Z[278]*Z[116]-Z[277]*Z[89])*Z[132];
  M[2][4] = -Z[140]*Z[278]*Z[136];
  M[2][5] = -(Z[279]*Z[141]-Z[280]*Z[146])*Z[149];
  M[2][6] = -(Z[279]*Z[160]-Z[280]*Z[181])*Z[195];
  M[2][7] = -Z[209]*Z[159]*Z[291];
}

void VP2_4_16_10_544_64_18_1::Calculate_M3()
{
  M[3][0] = (Z[296]*Z[15]+Z[297]*Z[24])*Z[32];
  M[3][1] = -(Z[297]*Z[36]+Z[298]*Z[40])*Z[53];
  M[3][2] = -Z[76]*Z[222]*Z[273];
  M[3][3] = -(Z[278]*Z[225]-Z[277]*Z[223])*Z[132];
  M[3][4] = -(Z[278]*Z[231]-Z[277]*Z[230])*Z[140];
  M[3][5] = -Z[149]*Z[279]*Z[235];
  M[3][6] = -(Z[279]*Z[242]-Z[280]*Z[244])*Z[195];
  M[3][7] = -(Z[241]*Z[291]-Z[239]*Z[285])*Z[209];
}

void VP2_4_16_10_544_64_18_1::Calculate_M12()
{
  M[12][0] = (Z[11]*Z[302]+Z[29]*Z[305])*Z[32];
  M[12][1] = -(Z[29]*Z[308]+Z[51]*Z[311])*Z[53];
  M[12][2] = -(Z[71]*Z[314]-Z[61]*Z[312])*Z[76];
  M[12][3] = -(Z[117]*Z[344]-Z[90]*Z[324])*Z[132];
  M[12][4] = -Z[140]*Z[117]*Z[355];
  M[12][5] = -(Z[142]*Z[356]-Z[147]*Z[357])*Z[149];
  M[12][6] = -(Z[142]*Z[364]-Z[147]*Z[380])*Z[195];
  M[12][7] = -Z[209]*Z[159]*Z[392];
}

void VP2_4_16_10_544_64_18_1::Calculate_M13()
{
  M[13][0] = (Z[212]*Z[302]+Z[216]*Z[305])*Z[32];
  M[13][1] = -(Z[216]*Z[308]+Z[220]*Z[311])*Z[53];
  M[13][2] = -Z[76]*Z[222]*Z[314];
  M[13][3] = -(Z[117]*Z[395]-Z[90]*Z[393])*Z[132];
  M[13][4] = -(Z[117]*Z[398]-Z[90]*Z[397])*Z[140];
  M[13][5] = -Z[149]*Z[142]*Z[399];
  M[13][6] = -(Z[142]*Z[400]-Z[147]*Z[402])*Z[195];
  M[13][7] = -(Z[241]*Z[392]-Z[239]*Z[390])*Z[209];
}

void VP2_4_16_10_544_64_18_1::Calculate_M14()
{
  M[14][0] = (Z[250]*Z[302]+Z[254]*Z[305])*Z[32];
  M[14][1] = -(Z[254]*Z[308]+Z[258]*Z[311])*Z[53];
  M[14][2] = -(Z[71]*Z[406]-Z[61]*Z[404])*Z[76];
  M[14][3] = -(Z[278]*Z[344]-Z[277]*Z[324])*Z[132];
  M[14][4] = -Z[140]*Z[278]*Z[355];
  M[14][5] = -(Z[279]*Z[356]-Z[280]*Z[357])*Z[149];
  M[14][6] = -(Z[279]*Z[364]-Z[280]*Z[380])*Z[195];
  M[14][7] = -Z[209]*Z[159]*Z[409];
}

void VP2_4_16_10_544_64_18_1::Calculate_M15()
{
  M[15][0] = (Z[295]*Z[302]+Z[297]*Z[305])*Z[32];
  M[15][1] = -(Z[297]*Z[308]+Z[299]*Z[311])*Z[53];
  M[15][2] = -Z[76]*Z[222]*Z[406];
  M[15][3] = -(Z[278]*Z[395]-Z[277]*Z[393])*Z[132];
  M[15][4] = -(Z[278]*Z[398]-Z[277]*Z[397])*Z[140];
  M[15][5] = -Z[149]*Z[279]*Z[399];
  M[15][6] = -(Z[279]*Z[400]-Z[280]*Z[402])*Z[195];
  M[15][7] = -(Z[241]*Z[409]-Z[239]*Z[407])*Z[209];
}

void VP2_4_16_10_544_64_18_1::Calculate_M16()
{
  M[16][2] = (Z[69]*Z[428]+Z[61]*Z[427])*Z[76];
  M[16][3] = -(Z[117]*Z[130]-Z[430]*Z[103])*Z[132];
  M[16][6] = -(Z[142]*Z[434]-Z[147]*Z[436])*Z[195];
  M[16][7] = (Z[433]*Z[205]+Z[432]*Z[200])*Z[209];
}

