<?php

/**
 * Created by PhpStorm.
 * User: kholz
 * Date: 8/9/20
 * Time: 11:18 AM
 */

$m = new MLabsCSVgen();
print $m;


class MLabsCSVgen
{

  public $labels = array(
      "Record Time",
      "L1","L2","L3",
      "L12","L23","L31",
      "I1","I2","I3",
      "In",
      "Freq.",
      "V-avr","U-avr","I-avr",
      "P","Q","S",
      "PF",
      "dI1","dI2","dI3",
      "dIo",
      "dkW","dkVAr",
      "THD L1","THD L2","THD L3",
      "THD L12","THD L23","THD L31",
      "THD I1","THD I2","THD I3",
      "THD In",
      "P1","P2","P3",
      "Q1","Q2","Q3",
      "kWh_Im","kWh_Ex",
      "kVArh-C","kVArh-I"
);

    function record_time($t){
        return sprintf('%02d:%02d:%02d', ($t/3600),($t/60%60), $t%60);
    }

    public $volt_120= array( 115, 125 );
    public $volt_spike_120 = 134;
    public $volt_drop_120 = 110;




    function volt_120() {
        switch (mt_rand(0,100)) {
            case 49 == mt_rand(45,55):
                $data=array($this->volt_drop_120, $this->volt_120[0]);
                break;
            case 50 == mt_rand(45,55):
                $data=array($this->volt_120[1], $this->volt_spike_120);
                break;
            case 51:
                $data=array($this->volt_120[0],$this->volt_120[1]);
            break;
            default:
                $data=array(120,122);
        }
        return mt_rand($data[0],$data[1]).".".mt_rand(0,9)." V";
    }



    public $volt_spike_208 = 230;
    public $volt_drop_208 = 200;
    public $volt_208= array( 206, 218 );
    function volt_208 () {
        switch (mt_rand(0,100)) {
            case 49:
                $data=array($this->volt_drop_208, $this->volt_208[0]);
                break;
            case 50:
                $data=array($this->volt_208[1], $this->volt_spike_208);
                break;
            case 51:
                $data=array($this->volt_208[0],$this->volt_208[1]);
                break;
            default:
                $data=array(208,208);
        }
        return mt_rand($data[0],$data[1]).".".mt_rand(0,9)." V";
    }



    public $amp_100 = array( 0, 99 );
    function amps_100 () {
        switch (mt_rand(0,100)) {
            case 49:
                $data=array(0, 15);
                break;
            case 50:
                $data=array(50, $this->amp_100[1]);
                break;
            case 51:
                $data=array($this->amp_100[0], 40);
                break;
            default:
                $data=array(20,25);
        }
        return mt_rand($data[0],$data[1]).".".mt_rand(0,9)." A";
    }






    /**
     * Example data is used as a place holder and/or input to generate a number within range
     *
     * @var array $data_example
     */

 public $data_example= array(
     // these are just fillers for now, may add calculators later on
     0.0,
     59.99,
     127.5,221.0,
     0.0,
     0.0,0.0,0.0,
     0.000,0.0,
     0.0,0.0,0.0,0.0,0.0,
     2.8,3.7,2.4,3.5,3.3,2.2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,190,0,30,28);

    /**
     * units used for each field
     * @var array $data_units
     */

    public $data_units= array(
        " A",
        " Hz",
        " V"," V"," A",
        " kW"," kVAr"," kVA",
        "", //PF
        " A"," A"," A",
        " A",
        " kW"," kVAr",
        "","","","","","","","","","",
        " kW"," kW"," kW",
        " kVAr"," kVAr"," kVAr",
        " kWh"," kWh",
        " kVArh"," kVArh"
 );

    /**
     * incrimant the time every 11s, up 24 hours
     * @var int $record
     */
    public $record=11;

    public $day_sec=86400;

    function __construct() {
        $day=$this->day_sec;
        $time=$this->record;
        while($day > $this->record){
            $this->add_row($time);
            $day=$day-$this->record;
            $time=$time+$this->record;
        }
    }

    function __toString() {
        $csv=join("\n", $this->CSV);
        return $csv;
    }

    public $CSV=array();
    function add_row($t) {
        $data[]=$this->record_time($t);
        $data[]=$this->volt_120();
        $data[]=$this->volt_120();
        $data[]=$this->volt_120();
        $data[]=$this->volt_208();
        $data[]=$this->volt_208();
        $data[]=$this->volt_208();
        $data[]=$this->amps_100();
        $data[]=$this->amps_100();
        $data[]=$this->amps_100();

        foreach($this->data_example as $k => $v) {
            $data[]=$this->data_example[$k].$this->data_units[$k];
        }

        $this->CSV[]='"'.join('";"',$data).'"';
        return TRUE;
    }
}