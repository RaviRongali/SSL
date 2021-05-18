function MD5 (input) {
  var rawHash = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, input);
  var txtHash = '';
  for (i = 0; i < rawHash.length; i++) {
    var hashVal = rawHash[i];
    if (hashVal < 0) {
      hashVal += 256;
    }
    if (hashVal.toString(16).length == 1) {
      txtHash += '0';
    }
    txtHash += hashVal.toString(16);
  }
  return txtHash;
}


function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('D1').activate()
  .setValue('Checksum_Input');
  spreadsheet.getRange('G1').activate()
  .setValue('md5checksum');
  spreadsheet.getActiveRangeList().clear({contentsOnly: true, skipFilteredRows: true});
  spreadsheet.getActiveRange().setValue('md5checksum');
  spreadsheet.getRange('G2').activate();
  spreadsheet.getActiveSheet().deleteColumns(spreadsheet.getActiveRange().getColumn(), spreadsheet.getActiveRange().getNumColumns());
  spreadsheet.getRange('G1').activate()
  .setValue('md5checksum');
  spreadsheet.getRange('G2').activate();
  spreadsheet.getCurrentCell().setFormula('=MD5(D2)');
  spreadsheet.getActiveRange().autoFill(spreadsheet.getRange('G2:G127'), SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES);
  spreadsheet.getRange('G2:G127').activate();
};
