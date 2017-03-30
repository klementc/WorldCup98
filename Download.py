import os


def main():

    print("Start to download data file!")

    files = ["http://ita.ee.lbl.gov/traces/WorldCup/wc_day1_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day2_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day3_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day4_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day5_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day6_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day7_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day8_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day9_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day10_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day11_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day12_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day13_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day14_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day15_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day16_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day17_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day18_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day19_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day20_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day21_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day22_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day23_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day24_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day25_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day26_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day27_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day28_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day29_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day30_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day31_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day32_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day33_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day34_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day35_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day36_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day37_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day38_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day38_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day39_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day39_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day40_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day40_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day41_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day41_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day42_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day43_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day44_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day44_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day44_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day45_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day45_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day45_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day46_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day47_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day48_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day49_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day49_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day49_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day49_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day50_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day50_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day50_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day50_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day51_9.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day52_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day53_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day54_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day55_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day55_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day55_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day55_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day55_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day56_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day56_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day56_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day57_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day57_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day57_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day58_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day59_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day60_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day61_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_9.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day62_10.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day63_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day63_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day63_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day63_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day64_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day64_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day64_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day65_9.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_8.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_9.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_10.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day66_11.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day67_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day67_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day67_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day67_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day67_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day68_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day68_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day68_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day69_7.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day70_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day70_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day70_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day71_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day71_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day72_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day72_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day72_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day73_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_5.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day74_6.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day75_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day75_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day75_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day76_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day76_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day77_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day77_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day78_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day78_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day79_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day79_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day79_3.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day79_4.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day80_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day80_2.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day81_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day82_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day83_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day84_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day85_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day86_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day87_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day88_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day89_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day90_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day91_1.gz",
             "http://ita.ee.lbl.gov/traces/WorldCup/wc_day92_1.gz"
             ]

    for file in files:
        os.system('wget ' + file)
        print(file)

if __name__ == "__main__":
    main()

